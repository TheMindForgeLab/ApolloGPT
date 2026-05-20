from apollo.db.repositories.base_repository import BaseRepository


class AgentIntelligenceRepository(BaseRepository):
    table = "agent_intelligence_profiles"
    id_prefix = "agent_intel"
    json_fields = ("skill_ids", "lora_profile_ids", "style_profile", "domain_packs", "metadata")
    allowed_fields = (
        "agent_id",
        "persona_id",
        "memory_policy_id",
        "skill_ids",
        "lora_profile_ids",
        "style_profile",
        "domain_packs",
        "system_instructions",
        "metadata",
    )

