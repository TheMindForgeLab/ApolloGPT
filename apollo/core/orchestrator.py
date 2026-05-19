from __future__ import annotations

from apollo.schemas import UserTask, to_dict


class Orchestrator:
    def __init__(self, task_router, memory_manager, context_builder, agent_controller, model_router, validator, logger):
        self.task_router = task_router
        self.memory_manager = memory_manager
        self.context_builder = context_builder
        self.agent_controller = agent_controller
        self.model_router = model_router
        self.validator = validator
        self.logger = logger

    def run_task(self, user_task: UserTask):
        task_analysis = self.task_router.analyze(user_task)
        memory_bundle = self.memory_manager.retrieve_relevant(
            query=user_task.input_text,
            project=task_analysis.project,
            task_type=task_analysis.task_type,
        )
        context_packet = self.context_builder.build(user_task, task_analysis, memory_bundle)
        agent = self.agent_controller.select_agent(task_analysis.required_agent)
        model = self.model_router.select_model(task_analysis)
        result = agent.run(context_packet=context_packet, model=model)
        validation = self.validator.validate(result, context_packet)
        stored_ids = self.memory_manager.store_result(user_task, result, validation)

        self.logger.event("task_completed", {
            "task": to_dict(user_task),
            "analysis": to_dict(task_analysis),
            "context_packet_id": context_packet.packet_id,
            "agent_id": result.agent_id,
            "model_id": result.model_id,
            "validation": {"success": validation.success, "score": validation.score, "issues": validation.issues},
            "stored_memory_ids": stored_ids,
        })

        return validation

