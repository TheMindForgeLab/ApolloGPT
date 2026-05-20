from __future__ import annotations

from apollo.agents.agent_registry import AgentRegistry
from apollo.agents.prompt_composer import AgentPromptComposer
from apollo.db.repositories.agent_intelligence_repository import AgentIntelligenceRepository
from apollo.db.repositories.agent_repository import AgentRepository
from apollo.db.repositories.lora_profile_repository import LoRAProfileRepository
from apollo.db.repositories.memory_policy_repository import MemoryPolicyRepository
from apollo.db.repositories.persona_repository import PersonaRepository
from apollo.db.repositories.skill_repository import SkillRepository


class AgentIntelligenceService:
    def __init__(self):
        self.agents = AgentRepository()
        self.agent_registry = AgentRegistry()
        self.personas = PersonaRepository()
        self.skills = SkillRepository()
        self.loras = LoRAProfileRepository()
        self.memory_policies = MemoryPolicyRepository()
        self.intelligence = AgentIntelligenceRepository()
        self.composer = AgentPromptComposer()

    def create_persona(self, payload: dict) -> dict:
        return self.personas.create({
            "name": payload["name"],
            "description": payload.get("description", ""),
            "tone": payload.get("tone", ""),
            "rules": payload.get("rules", []),
            "examples": payload.get("examples", []),
            "metadata": payload.get("metadata", {}),
        })

    def create_skill(self, payload: dict) -> dict:
        return self.skills.create({
            "name": payload["name"],
            "description": payload.get("description", ""),
            "skill_type": payload.get("skill_type", "general"),
            "instructions": payload.get("instructions", ""),
            "tools": payload.get("tools", []),
            "input_types": payload.get("input_types", []),
            "output_types": payload.get("output_types", []),
            "metadata": payload.get("metadata", {}),
        })

    def create_lora(self, payload: dict) -> dict:
        return self.loras.create({
            "name": payload["name"],
            "lora_type": payload.get("lora_type", "text"),
            "base_model": payload.get("base_model", ""),
            "trigger_phrase": payload.get("trigger_phrase", ""),
            "strength": payload.get("strength", 1.0),
            "adapter_path": payload.get("adapter_path", ""),
            "allowed_models": payload.get("allowed_models", []),
            "metadata": payload.get("metadata", {}),
        })

    def create_memory_policy(self, payload: dict) -> dict:
        return self.memory_policies.create({
            "name": payload["name"],
            "scopes": payload.get("scopes", ["project", "agent"]),
            "retrieval_limit": payload.get("retrieval_limit", 8),
            "include_summaries": int(bool(payload.get("include_summaries", True))),
            "include_graph": int(bool(payload.get("include_graph", True))),
            "include_files": int(bool(payload.get("include_files", True))),
            "rules": payload.get("rules", []),
            "metadata": payload.get("metadata", {}),
        })

    def create_custom_agent(self, payload: dict) -> dict:
        agent = self.agent_registry.create_agent(payload)
        intelligence = self.intelligence.create({
            "agent_id": agent["id"],
            "persona_id": payload.get("persona_id"),
            "memory_policy_id": payload.get("memory_policy_id"),
            "skill_ids": payload.get("skill_ids", []),
            "lora_profile_ids": payload.get("lora_profile_ids", []),
            "style_profile": payload.get("style_profile", {}),
            "domain_packs": payload.get("domain_packs", []),
            "system_instructions": payload.get("system_instructions", ""),
            "metadata": payload.get("intelligence_metadata", {}),
        })
        return {"agent": agent, "intelligence": intelligence, "composed_prompt": self.compose_prompt(agent["id"])}

    def compose_prompt(self, agent_id: str) -> str:
        agent = self.agents.get(agent_id)
        profiles = self.intelligence.list({"agent_id": agent_id})
        intelligence = profiles[0] if profiles else {}
        persona = self.personas.get(intelligence.get("persona_id")) if intelligence.get("persona_id") else None
        memory_policy = self.memory_policies.get(intelligence.get("memory_policy_id")) if intelligence.get("memory_policy_id") else None
        skills = [self.skills.get(skill_id) for skill_id in intelligence.get("skill_ids", [])]
        loras = [self.loras.get(lora_id) for lora_id in intelligence.get("lora_profile_ids", [])]
        return self.composer.compose(
            agent=agent or {},
            intelligence=intelligence,
            persona=persona,
            skills=[skill for skill in skills if skill],
            loras=[lora for lora in loras if lora],
            memory_policy=memory_policy,
        )

    def inventory(self) -> dict:
        return {
            "personas": self.personas.list(),
            "skills": self.skills.list(),
            "loras": self.loras.list(),
            "memory_policies": self.memory_policies.list(),
            "agent_intelligence_profiles": self.intelligence.list(),
        }

