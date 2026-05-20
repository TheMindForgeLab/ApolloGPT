from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apollo.agents.intelligence_service import AgentIntelligenceService


def main() -> None:
    service = AgentIntelligenceService()
    persona = service.create_persona({
        "name": "Phase 3 Writer Persona",
        "description": "Portable writing behavior for multiple LLMs.",
        "tone": "precise, structured, useful",
        "rules": ["Use memory first", "Preserve voice", "Avoid generic filler"],
        "examples": ["Example: concise but complete writing."],
    })
    skill = service.create_skill({
        "name": "Memory-Aware Longform Writing",
        "skill_type": "writing",
        "description": "Drafts long-form outputs from scoped memory.",
        "instructions": "Retrieve relevant memory, infer structure, draft, and self-check.",
        "tools": ["memory_search", "document_builder"],
        "input_types": ["brief", "files", "memory"],
        "output_types": ["markdown", "doc"],
    })
    lora = service.create_lora({
        "name": "Phase 3 Style Adapter",
        "lora_type": "text",
        "base_model": "any-local-llm",
        "trigger_phrase": "phase3style",
        "strength": 0.75,
        "allowed_models": ["ollama", "lmstudio", "vllm"],
    })
    memory_policy = service.create_memory_policy({
        "name": "Writer Agent RAG Policy",
        "scopes": ["business", "department", "project", "agent"],
        "retrieval_limit": 12,
        "rules": ["Prefer style examples", "Include project decisions"],
    })
    result = service.create_custom_agent({
        "name": "Phase 3 Adaptive Writer",
        "agent_type": "writer",
        "role": "Writes with persona, skills, LoRA adapters, and scoped memory.",
        "preferred_model": "auto",
        "memory_access": ["business", "department", "project", "agent"],
        "tool_access": ["memory_search", "document_builder"],
        "workflow_permissions": ["draft", "revise", "handoff"],
        "persona_id": persona["id"],
        "skill_ids": [skill["id"]],
        "lora_profile_ids": [lora["id"]],
        "memory_policy_id": memory_policy["id"],
        "style_profile": {"format": "markdown", "voice": "portable across LLMs"},
    })
    prompt = result["composed_prompt"]
    assert "Phase 3 Adaptive Writer" in prompt
    assert "Phase 3 Writer Persona" in prompt
    assert "Memory-Aware Longform Writing" in prompt
    assert "Phase 3 Style Adapter" in prompt
    assert "business, department, project, agent" in prompt

    print("Phase 3 agent intelligence smoke test passed.")
    print(f"Agent: {result['agent']['name']}")
    print(f"Persona: {persona['name']}")
    print(f"Skill: {skill['name']}")
    print(f"LoRA: {lora['name']}")


if __name__ == "__main__":
    main()

