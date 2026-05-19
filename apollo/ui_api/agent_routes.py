from __future__ import annotations

from fastapi import APIRouter, HTTPException

from apollo.agents.agent_registry import AgentRegistry

router = APIRouter(prefix="/api/agents", tags=["agents"])
registry = AgentRegistry()


@router.get("")
def list_agents(business_id: str | None = None, department_id: str | None = None):
    saved = registry.list_saved_agents({"business_id": business_id, "department_id": department_id})
    built_in = [{"key": key, "agent_id": agent.agent_id, "name": agent.name, "role": agent.role} for key, agent in registry.agents.items()]
    return {"items": saved, "built_in": built_in}


@router.post("")
def create_agent(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Agent name is required.")
    return {"agent": registry.create_agent(payload)}
