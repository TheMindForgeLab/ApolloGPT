from __future__ import annotations

from apollo.schemas import AgentResult, ContextPacket, ValidationResult


class Validator:
    def validate(self, result: AgentResult, context_packet: ContextPacket) -> ValidationResult:
        issues: list[str] = []
        output = result.output.strip()

        if not output:
            issues.append("Output was empty.")
        if not result.success:
            issues.append("Agent reported failure.")
        if context_packet.task.input_text and len(output) < 10:
            issues.append("Output appears too short for the task.")

        score = max(0.0, 1.0 - (0.25 * len(issues)))
        return ValidationResult(output=output, success=not issues, issues=issues, score=score, raw_result=result)

