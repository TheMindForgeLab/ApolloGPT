from __future__ import annotations

from apollo.schemas import UserTask


class WorkflowRunner:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator

    def run(self, workflow):
        results = []
        for step in workflow.steps:
            task = UserTask(input_text=step.instruction, project=step.project, metadata={"workflow": workflow.name, "step": step.name})
            results.append(self.orchestrator.run_task(task))
        return results

