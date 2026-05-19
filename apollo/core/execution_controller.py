class ExecutionController:
    def execute(self, agent, context_packet, model):
        return agent.run(context_packet=context_packet, model=model)

