from __future__ import annotations


class AgentPromptComposer:
    def compose(self, agent: dict, intelligence: dict | None = None, persona: dict | None = None, skills: list[dict] | None = None, loras: list[dict] | None = None, memory_policy: dict | None = None) -> str:
        intelligence = intelligence or {}
        skills = skills or []
        loras = loras or []

        lines = [
            f"You are {agent.get('name', 'Apollo Agent')}.",
            f"Role: {agent.get('role', '')}",
            f"Agent type: {agent.get('agent_type', 'specialist')}",
        ]

        if persona:
            lines.extend([
                "",
                "Persona:",
                f"- Name: {persona.get('name', '')}",
                f"- Tone: {persona.get('tone', '')}",
                f"- Description: {persona.get('description', '')}",
            ])
            for rule in persona.get("rules", []):
                lines.append(f"- Rule: {rule}")

        style = intelligence.get("style_profile") or {}
        if style:
            lines.extend(["", "Writing / behavior style:"])
            for key, value in style.items():
                lines.append(f"- {key}: {value}")

        if skills:
            lines.extend(["", "Skills enabled:"])
            for skill in skills:
                lines.append(f"- {skill.get('name')}: {skill.get('description', '')}")
                if skill.get("instructions"):
                    lines.append(f"  Instructions: {skill['instructions']}")

        if loras:
            lines.extend(["", "LoRA / adapter stack:"])
            for lora in loras:
                lines.append(
                    f"- {lora.get('name')} ({lora.get('lora_type', 'text')}), trigger={lora.get('trigger_phrase', '')}, strength={lora.get('strength', 1.0)}"
                )

        if memory_policy:
            lines.extend(["", "Memory/RAG policy:"])
            lines.append(f"- Scopes: {', '.join(memory_policy.get('scopes', []))}")
            lines.append(f"- Retrieval limit: {memory_policy.get('retrieval_limit', 8)}")
            for rule in memory_policy.get("rules", []):
                lines.append(f"- Rule: {rule}")

        if intelligence.get("system_instructions"):
            lines.extend(["", "Additional system instructions:", intelligence["system_instructions"]])

        lines.extend([
            "",
            "Use the context packet, retrieved memory, allowed tools, and model router. Keep the output aligned with the active persona, style, skills, memory policy, and project goal.",
        ])
        return "\n".join(lines)

