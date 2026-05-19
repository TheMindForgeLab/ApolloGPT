from __future__ import annotations

from apollo.schemas import AgentResult, ContextPacket


class AgentBase:
    agent_id = "base"
    name = "Base Agent"
    role = "General execution"

    def build_prompt(self, context_packet: ContextPacket) -> str:
        memory_lines = "\n".join(f"- {item.content[:500]}" for item in context_packet.relevant_memories[:8])
        return f"""You are {self.name}.
Role: {self.role}

Task:
{context_packet.task.input_text}

Project:
{context_packet.task.project}

Task analysis:
- type: {context_packet.task_analysis.task_type}
- intent: {context_packet.task_analysis.intent}
- complexity: {context_packet.task_analysis.complexity}

Project context:
{context_packet.project_context or "No summary yet."}

Relevant memory:
{memory_lines or "No retrieved memory yet."}

Constraints:
{chr(10).join(f"- {item}" for item in context_packet.constraints)}

Return a practical, structured answer that moves the project forward.
"""

    def run(self, context_packet: ContextPacket, model) -> AgentResult:
        prompt = self.build_prompt(context_packet)
        output = model.generate(prompt)
        return AgentResult(
            output=output,
            reasoning_summary=f"{self.name} used a context packet and {model.model_id}.",
            tool_calls=[],
            memories_to_store=[],
            success=bool(output.strip()),
            agent_id=self.agent_id,
            model_id=model.model_id,
        )

