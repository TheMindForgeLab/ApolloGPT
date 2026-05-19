class WorkflowRegistry:
    def __init__(self):
        self.workflows = {}

    def list(self):
        return list(self.workflows.values())

    def register(self, workflow):
        self.workflows[workflow.name] = workflow
        return workflow
