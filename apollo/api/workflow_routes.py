from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix="/workflows", tags=["workflows"])


@router.get("")
def list_workflows():
    return {
        "templates": [
            "research_to_summary",
            "content_pipeline",
            "coding_task",
            "automation_design",
        ]
    }

