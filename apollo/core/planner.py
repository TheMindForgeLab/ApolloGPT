class Planner:
    def plan(self, task_analysis):
        return {"steps": ["retrieve_memory", "build_context", "execute_agent", "validate", "store_memory"], "task_type": task_analysis.task_type}

