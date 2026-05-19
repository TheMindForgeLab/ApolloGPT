from __future__ import annotations

from apollo.agents.automation_agent import AutomationAgent
from apollo.agents.developer_agent import DeveloperAgent
from apollo.agents.manager_agent import ManagerAgent
from apollo.agents.researcher_agent import ResearcherAgent
from apollo.agents.writer_agent import WriterAgent


class AgentController:
    def __init__(self):
        self.agents = {
            "writer": WriterAgent(),
            "developer": DeveloperAgent(),
            "researcher": ResearcherAgent(),
            "manager": ManagerAgent(),
            "automation": AutomationAgent(),
        }

    def select_agent(self, agent_name: str):
        return self.agents.get(agent_name, self.agents["manager"])

