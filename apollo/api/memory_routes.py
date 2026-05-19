from __future__ import annotations

from fastapi import APIRouter

from apollo.memory.memory_manager import MemoryManager
from apollo.settings import settings

router = APIRouter(prefix="/memory", tags=["memory"])
memory = MemoryManager(settings.storage_dir)


@router.post("/search")
def search(payload: dict):
    bundle = memory.retrieve_relevant(payload.get("query", ""), project=payload.get("project"), task_type=payload.get("task_type"))
    return {
        "memories": [item.__dict__ for item in bundle["memories"]],
        "summary": bundle["summaries"],
        "graph_context": bundle["graph_context"],
        "preferences": bundle["preferences"],
    }

