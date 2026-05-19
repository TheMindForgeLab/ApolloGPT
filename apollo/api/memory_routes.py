from __future__ import annotations

from fastapi import APIRouter

from apollo.memory.memory_manager import MemoryManager
from apollo.settings import settings

router = APIRouter(prefix="/memory", tags=["memory"])
memory = MemoryManager(settings.storage_dir)


@router.post("/search")
def search(payload: dict):
    bundle = memory.retrieve_relevant(
        payload.get("query", ""),
        project=payload.get("project"),
        task_type=payload.get("task_type"),
        limit=int(payload.get("limit", 8)),
    )
    return {
        "memories": [item.__dict__ for item in bundle["memories"]],
        "summary": bundle["summaries"],
        "graph_context": bundle["graph_context"],
        "preferences": bundle["preferences"],
        "retrieval": bundle["retrieval"],
    }


@router.post("/ingest-text")
def ingest_text(payload: dict):
    text = payload.get("text", "")
    if not text.strip():
        return {"memory_ids": [], "chunks": 0}
    ids = memory.ingest_text(
        text,
        project=payload.get("project"),
        source=payload.get("source", "api"),
        memory_type=payload.get("memory_type", "document"),
        metadata=payload.get("metadata", {}),
    )
    return {"memory_ids": ids, "chunks": len(ids)}
