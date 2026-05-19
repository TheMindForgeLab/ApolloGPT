class Retriever:
    def __init__(self, memory_manager):
        self.memory_manager = memory_manager

    def retrieve(self, query, project=None, task_type=None):
        return self.memory_manager.retrieve_relevant(query=query, project=project, task_type=task_type)
