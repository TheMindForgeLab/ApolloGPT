from __future__ import annotations

from apollo.db.repositories.agent_repository import AgentRepository
from apollo.db.repositories.business_repository import BusinessRepository
from apollo.db.repositories.department_repository import DepartmentRepository
from apollo.db.repositories.project_repository import ProjectRepository
from apollo.db.repositories.task_repository import TaskRepository


DEFAULT_DEPARTMENTS = [
    {"name": "Research", "purpose": "Gather, verify, and synthesize useful information."},
    {"name": "Content", "purpose": "Write, edit, and package content outputs."},
    {"name": "Operations", "purpose": "Coordinate tasks, processes, and execution state."},
    {"name": "Media", "purpose": "Generate and manage visual, audio, and brand assets."},
    {"name": "Automation", "purpose": "Build triggers, workflows, integrations, and scheduled actions."},
]


class BusinessManager:
    def __init__(self):
        self.businesses = BusinessRepository()
        self.departments = DepartmentRepository()
        self.projects = ProjectRepository()
        self.agents = AgentRepository()
        self.tasks = TaskRepository()

    def create_business(self, payload: dict) -> dict:
        generate_starter = bool(payload.get("generate_starter", True))
        business = self.businesses.create({
            "name": payload["name"],
            "business_type": payload.get("business_type", "Custom"),
            "purpose": payload.get("purpose", ""),
            "goals": payload.get("goals", []),
            "brand_voice": payload.get("brand_voice", ""),
            "constraints": payload.get("constraints", []),
            "metadata": payload.get("metadata", {}),
        })
        created = {"business": business, "departments": [], "agents": [], "projects": [], "tasks": []}

        if generate_starter:
            created.update(self._create_starter_structure(business))
        return created

    def _create_starter_structure(self, business: dict) -> dict:
        departments = []
        agents = []
        for department_template in DEFAULT_DEPARTMENTS:
            department = self.departments.create({
                "business_id": business["id"],
                "name": department_template["name"],
                "purpose": department_template["purpose"],
                "allowed_tools": ["memory_search", "file_system", "workflow_runner"],
            })
            departments.append(department)
            agent = self.agents.create({
                "business_id": business["id"],
                "department_id": department["id"],
                "name": f"{department['name']} Agent",
                "agent_type": "department_worker",
                "role": department["purpose"],
                "preferred_model": "auto",
                "memory_access": ["business", "department", "project"],
                "tool_access": ["memory_search", "file_system"],
                "workflow_permissions": ["run_department_workflows"],
            })
            agents.append(agent)

        project = self.projects.create({
            "business_id": business["id"],
            "name": f"{business['name']} Launch Project",
            "goal": f"Set up the first operating project for {business['name']}.",
            "status": "active",
        })
        tasks = [
            self.tasks.create({
                "business_id": business["id"],
                "project_id": project["id"],
                "title": "Define operating goals",
                "description": "Clarify the first outcomes this business should produce.",
                "priority": "high",
            }),
            self.tasks.create({
                "business_id": business["id"],
                "project_id": project["id"],
                "title": "Review starter departments and agents",
                "description": "Adjust the generated departments, agents, tools, and memory scopes.",
                "priority": "normal",
            }),
        ]
        return {"departments": departments, "agents": agents, "projects": [project], "tasks": tasks}

    def list_businesses(self) -> list[dict]:
        return self.businesses.list()

    def get_business_dashboard(self, business_id: str) -> dict | None:
        business = self.businesses.get(business_id)
        if not business:
            return None
        return {
            "business": business,
            "departments": self.departments.list({"business_id": business_id}),
            "projects": self.projects.list({"business_id": business_id}),
            "agents": self.agents.list({"business_id": business_id}),
            "tasks": self.tasks.list({"business_id": business_id}),
        }
