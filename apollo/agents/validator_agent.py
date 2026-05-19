from apollo.agents.base_agent import AgentBase


class ValidatorAgent(AgentBase):
    agent_id = "agent_validator"
    name = "Validator Agent"
    role = "Checks quality, correctness, completeness, and risk."

