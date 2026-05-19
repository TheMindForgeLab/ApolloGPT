from __future__ import annotations

from apollo.db.repositories.agent_repository import AgentRepository
from apollo.db.repositories.department_repository import DepartmentRepository
from apollo.db.repositories.task_repository import TaskRepository


class DepartmentManager:
    def __init__(self):
        self.departments = DepartmentRepository()
        self.agents = AgentRepository()
        self.tasks = TaskRepository()

    def create_department(self, payload: dict) -> dict:
        department = self.departments.create({
            "business_id": payload["business_id"],
            "name": payload["name"],
            "purpose": payload.get("purpose", ""),
            "manager_agent_id": payload.get("manager_agent_id"),
            "allowed_tools": payload.get("allowed_tools", []),
            "memory_scope": payload.get("memory_scope", "department"),
            "metadata": payload.get("metadata", {}),
        })
        return {"department": department}

    def dashboard(self, department_id: str) -> dict | None:
        department = self.departments.get(department_id)
        if not department:
            return None
        return {
            "department": department,
            "agents": self.agents.list({"department_id": department_id}),
            "tasks": self.tasks.list({"department_id": department_id}),
        }
