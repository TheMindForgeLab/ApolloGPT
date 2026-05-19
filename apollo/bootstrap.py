from __future__ import annotations

from apollo.agents.agent_controller import AgentController
from apollo.core.context_packet_builder import ContextPacketBuilder
from apollo.core.logger import ApolloLogger
from apollo.core.orchestrator import Orchestrator
from apollo.core.task_router import TaskRouter
from apollo.core.validator import Validator
from apollo.memory.memory_manager import MemoryManager
from apollo.models.model_router import ModelRouter
from apollo.settings import settings


def build_orchestrator() -> Orchestrator:
    settings.storage_dir.mkdir(parents=True, exist_ok=True)
    return Orchestrator(
        task_router=TaskRouter(),
        memory_manager=MemoryManager(settings.storage_dir),
        context_builder=ContextPacketBuilder(),
        agent_controller=AgentController(),
        model_router=ModelRouter(settings),
        validator=Validator(),
        logger=ApolloLogger(settings.storage_dir),
    )

