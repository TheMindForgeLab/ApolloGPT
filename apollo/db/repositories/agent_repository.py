from apollo.db.repositories.base_repository import BaseRepository


class AgentRepository(BaseRepository):
    table = "agents"
    id_prefix = "agent"
    json_fields = ("memory_access", "tool_access", "workflow_permissions", "metadata")
    allowed_fields = (
        "business_id",
        "department_id",
        "name",
        "agent_type",
        "role",
        "persona",
        "preferred_model",
        "fallback_model",
        "memory_access",
        "tool_access",
        "workflow_permissions",
        "lora_profile",
        "status",
        "metadata",
    )
