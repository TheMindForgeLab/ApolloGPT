from __future__ import annotations

from apollo.schemas import ContextPacket, MemoryItem, TaskAnalysis, UserTask, new_id


class ContextPacketBuilder:
    def build(self, user_task: UserTask, task_analysis: TaskAnalysis, memory_bundle: dict) -> ContextPacket:
        memories: list[MemoryItem] = memory_bundle.get("memories", [])
        summaries = memory_bundle.get("summaries", "")
        preferences = memory_bundle.get("preferences", {})

        constraints = [
            "local-first by default",
            "memory-centric: use retrieved memory when relevant",
            "return practical buildable output",
            "log results and store useful lessons",
        ]

        return ContextPacket(
            packet_id=new_id("ctx"),
            task=user_task,
            task_analysis=task_analysis,
            agent_role=task_analysis.required_agent,
            relevant_memories=memories,
            project_context=summaries,
            user_preferences=preferences,
            constraints=constraints,
            tools_available=task_analysis.required_tools,
        )

