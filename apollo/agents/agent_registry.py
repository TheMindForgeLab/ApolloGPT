from __future__ import annotations


from apollo.agents.agent_controller import AgentController
from apollo.db.repositories.agent_repository import AgentRepository


class AgentRegistry(AgentController):
    def __init__(self):
        super().__init__()
        self.repository = AgentRepository()

    def create_agent(self, payload: dict) -> dict:
        return self.repository.create({
            "business_id": payload.get("business_id"),
            "department_id": payload.get("department_id"),
            "name": payload["name"],
            "agent_type": payload.get("agent_type", "specialist"),
            "role": payload.get("role", ""),
            "persona": payload.get("persona", ""),
            "preferred_model": payload.get("preferred_model", "auto"),
            "fallback_model": payload.get("fallback_model", ""),
            "memory_access": payload.get("memory_access", ["project"]),
            "tool_access": payload.get("tool_access", []),
            "workflow_permissions": payload.get("workflow_permissions", []),
            "lora_profile": payload.get("lora_profile", ""),
            "metadata": payload.get("metadata", {}),
        })

    def list_saved_agents(self, filters: dict | None = None) -> list[dict]:
        return self.repository.list(filters or {})

