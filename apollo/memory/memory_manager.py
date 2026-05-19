from __future__ import annotations

from apollo.memory.graph_memory import GraphMemory
from apollo.memory.memory_indexer import MemoryIndexer
from apollo.memory.preference_memory import PreferenceMemory
from apollo.memory.raw_memory import RawMemory
from apollo.memory.summary_memory import SummaryMemory
from apollo.memory.vector_memory import VectorMemory
from apollo.schemas import AgentResult, UserTask, ValidationResult, to_dict, utc_now


class MemoryManager:
    def __init__(self, storage_dir):
        self.raw = RawMemory(storage_dir)
        self.vector = VectorMemory(storage_dir)
        self.graph = GraphMemory(storage_dir)
        self.summary = SummaryMemory(storage_dir)
        self.preferences = PreferenceMemory(storage_dir)
        self.indexer = MemoryIndexer(self.vector)

    def ingest_text(self, text: str, project=None, source: str = "manual", memory_type: str = "document", metadata: dict | None = None) -> list[str]:
        metadata = {"source": source, **(metadata or {})}
        memory_ids = self.indexer.index_text(text, project=project, memory_type=memory_type, metadata=metadata)
        if project:
            self.summary.update_from_result(project, f"Ingested source: {source}\nChunks: {len(memory_ids)}")
            self.graph.add_relationship(project, "ingested_source", source, {"chunks": len(memory_ids)})
        return memory_ids

    def retrieve_relevant(self, query: str, project=None, task_type=None, limit: int = 8) -> dict:
        memories = self.vector.search(query, project=project, limit=limit)
        return {
            "memories": memories,
            "summaries": self.summary.get_project_summary(project),
            "graph_context": self.graph.get_related(project),
            "preferences": self.preferences.get_active_preferences(),
            "task_type": task_type,
            "retrieval": {
                "query": query,
                "project": project,
                "limit": limit,
                "count": len(memories),
            },
        }

    def store_result(self, user_task: UserTask, result: AgentResult, validation: ValidationResult) -> list[str]:
        record = {
            "timestamp": utc_now(),
            "task": to_dict(user_task),
            "result": to_dict(result),
            "validation": {
                "success": validation.success,
                "score": validation.score,
                "issues": validation.issues,
            },
        }
        self.raw.append(record)
        memory_ids = [
            self.vector.add_text(
                result.output,
                project=user_task.project,
                memory_type="outcome",
                metadata={"task_id": user_task.id, "agent_id": result.agent_id, "model_id": result.model_id},
            )
        ]
        self.summary.update_from_result(user_task.project, f"Task: {user_task.input_text}\nOutput: {result.output}")
        self.graph.add_relationship(user_task.project or "global", "produced_task", user_task.id)
        return memory_ids
