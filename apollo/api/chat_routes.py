from __future__ import annotations

from fastapi import APIRouter

from apollo.bootstrap import build_orchestrator
from apollo.schemas import UserTask

router = APIRouter(prefix="/chat", tags=["chat"])
orchestrator = build_orchestrator()


@router.post("")
def chat(payload: dict):
    task = UserTask(input_text=payload.get("message", ""), project=payload.get("project", "ApolloGPT"))
    result = orchestrator.run_task(task)
    return {"response": result.output, "success": result.success, "agent_id": result.raw_result.agent_id, "model_id": result.raw_result.model_id}

