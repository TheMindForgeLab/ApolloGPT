from __future__ import annotations

from apollo.schemas import TaskAnalysis, UserTask


class TaskRouter:
    """Rule-based router first; replace with local classifier later."""

    def analyze(self, user_task: UserTask) -> TaskAnalysis:
        text = user_task.input_text.lower()
        required_tools: list[str] = []

        if any(word in text for word in ["code", "python", "debug", "file", "repo", "backend", "api"]):
            return TaskAnalysis("coding", "developer", "coding", required_tools, user_task.project, "medium", "implementation")
        if any(word in text for word in ["research", "find", "compare", "source", "fact"]):
            return TaskAnalysis("research", "researcher", "reasoning", ["memory_search"], user_task.project, "medium", "research")
        if any(word in text for word in ["write", "draft", "article", "whitepaper", "post", "script"]):
            return TaskAnalysis("writing", "writer", "writing", required_tools, user_task.project, "medium", "content")
        if any(word in text for word in ["workflow", "automation", "n8n", "schedule", "trigger"]):
            return TaskAnalysis("automation", "automation", "reasoning", ["workflow_runner"], user_task.project, "high", "automation")
        if any(word in text for word in ["plan", "roadmap", "break down", "project"]):
            return TaskAnalysis("planning", "manager", "reasoning", required_tools, user_task.project, "medium", "planning")

        return TaskAnalysis("general", "manager", "default", required_tools, user_task.project, "low", "general")

