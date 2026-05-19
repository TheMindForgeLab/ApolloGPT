from __future__ import annotations

from fastapi import APIRouter

from apollo.agents.agent_controller import AgentController

router = APIRouter(prefix="/agents", tags=["agents"])
controller = AgentController()


@router.get("")
def list_agents():
    return [{"key": key, "agent_id": agent.agent_id, "name": agent.name, "role": agent.role} for key, agent in controller.agents.items()]

