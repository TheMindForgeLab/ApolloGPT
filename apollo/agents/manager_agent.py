from apollo.agents.base_agent import AgentBase


class ManagerAgent(AgentBase):
    agent_id = "agent_manager"
    name = "Project Manager Agent"
    role = "Breaks work into tasks, coordinates agents, plans roadmaps, and tracks progress."

