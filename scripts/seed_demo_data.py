from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apollo.agents.agent_registry import AgentRegistry
from apollo.automations.automation_manager import AutomationManager
from apollo.businesses.business_manager import BusinessManager
from apollo.db.repositories.department_repository import DepartmentRepository
from apollo.db.repositories.project_repository import ProjectRepository


AGENT_ROLES = [
    ("Research Agent", "Finds, verifies, and summarizes information."),
    ("Writer Agent", "Drafts content, docs, books, posts, and scripts."),
    ("Editor Agent", "Reviews quality, structure, tone, and clarity."),
    ("Coder Agent", "Builds, debugs, and refactors code."),
    ("Media Agent", "Creates image, video, audio, and brand asset prompts."),
    ("Automation Agent", "Builds triggers, schedules, webhooks, and workflows."),
    ("Analyst Agent", "Analyzes metrics, performance, and decisions."),
    ("Validator Agent", "Checks accuracy, completeness, and policy constraints."),
    ("Planner Agent", "Breaks goals into execution plans."),
    ("Customer Agent", "Handles customer support and response flows."),
    ("Sales Agent", "Creates offers, outreach, and follow-up tasks."),
    ("Operations Agent", "Tracks execution state and handoffs."),
]


def main() -> None:
    business_manager = BusinessManager()
    result = business_manager.create_business({
        "name": "ApolloGPT Demo Operating Company",
        "business_type": "AI Operating System",
        "purpose": "Demonstrate many agents, departments, projects, tasks, and automations.",
        "goals": ["Run dozens of agents", "Coordinate automations", "Use local model routing"],
        "generate_starter": True,
    })
    business = result["business"]
    departments = DepartmentRepository().list({"business_id": business["id"]})
    projects = ProjectRepository().list({"business_id": business["id"]})
    first_department = departments[0] if departments else None
    first_project = projects[0] if projects else None

    registry = AgentRegistry()
    created_agents = []
    for index in range(24):
        name, role = AGENT_ROLES[index % len(AGENT_ROLES)]
        created_agents.append(registry.create_agent({
            "business_id": business["id"],
            "department_id": first_department["id"] if first_department else None,
            "name": f"{name} {index + 1}",
            "agent_type": "specialist",
            "role": role,
            "preferred_model": "auto",
            "memory_access": ["business", "department", "project", "agent"],
            "tool_access": ["memory_search", "file_system", "workflow_runner"],
            "workflow_permissions": ["run", "handoff", "request_approval"],
        }))

    automation_manager = AutomationManager()
    automations = [
        automation_manager.create({
            "business_id": business["id"],
            "project_id": first_project["id"] if first_project else None,
            "name": "Daily Memory Summary",
            "trigger": {"type": "schedule", "cron": "0 18 * * *"},
            "workflow_name": "daily_memory_summary",
            "approval_required": False,
            "status": "active",
        }),
        automation_manager.create({
            "business_id": business["id"],
            "project_id": first_project["id"] if first_project else None,
            "name": "New File Ingestion",
            "trigger": {"type": "file_uploaded"},
            "workflow_name": "file_ingestion_pipeline",
            "approval_required": False,
            "status": "draft",
        }),
        automation_manager.create({
            "business_id": business["id"],
            "project_id": first_project["id"] if first_project else None,
            "name": "Content Workflow Draft",
            "trigger": {"type": "chat_command", "command": "create content"},
            "workflow_name": "content_pipeline",
            "approval_required": True,
            "status": "draft",
        }),
    ]

    print("Seed demo data created.")
    print(f"Business: {business['name']}")
    print(f"Extra agents: {len(created_agents)}")
    print(f"Automations: {len(automations)}")


if __name__ == "__main__":
    main()
