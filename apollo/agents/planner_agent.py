from apollo.agents.manager_agent import ManagerAgent


class PlannerAgent(ManagerAgent):
    agent_id = "agent_planner"
    name = "Planner Agent"
    role = "Turns goals into phased plans, milestones, and execution steps."

