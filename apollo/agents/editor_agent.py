from apollo.agents.base_agent import AgentBase


class EditorAgent(AgentBase):
    agent_id = "agent_editor"
    name = "Editor Agent"
    role = "Reviews, improves, and polishes written output."

