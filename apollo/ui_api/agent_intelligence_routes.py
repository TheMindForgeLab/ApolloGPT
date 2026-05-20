from __future__ import annotations

from fastapi import APIRouter, HTTPException

from apollo.agents.intelligence_service import AgentIntelligenceService

router = APIRouter(prefix="/api/agent-intelligence", tags=["agent-intelligence"])
service = AgentIntelligenceService()


@router.get("")
def inventory():
    return service.inventory()


@router.post("/personas")
def create_persona(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Persona name is required.")
    return {"persona": service.create_persona(payload)}


@router.post("/skills")
def create_skill(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Skill name is required.")
    return {"skill": service.create_skill(payload)}


@router.post("/loras")
def create_lora(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="LoRA profile name is required.")
    return {"lora": service.create_lora(payload)}


@router.post("/memory-policies")
def create_memory_policy(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Memory policy name is required.")
    return {"memory_policy": service.create_memory_policy(payload)}


@router.post("/agents")
def create_custom_agent(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Agent name is required.")
    return service.create_custom_agent(payload)


@router.get("/agents/{agent_id}/prompt")
def compose_agent_prompt(agent_id: str):
    return {"agent_id": agent_id, "prompt": service.compose_prompt(agent_id)}

