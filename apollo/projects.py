from __future__ import annotations

from apollo.db.repositories.project_repository import ProjectRepository
from apollo.db.repositories.task_repository import TaskRepository


class ProjectManager:
    def __init__(self):
        self.projects = ProjectRepository()
        self.tasks = TaskRepository()

    def create_project(self, payload: dict) -> dict:
        project = self.projects.create({
            "business_id": payload.get("business_id"),
            "department_id": payload.get("department_id"),
            "name": payload["name"],
            "goal": payload.get("goal", ""),
            "status": payload.get("status", "active"),
            "metadata": payload.get("metadata", {}),
        })
        return {"project": project}

    def dashboard(self, project_id: str) -> dict | None:
        project = self.projects.get(project_id)
        if not project:
            return None
        return {"project": project, "tasks": self.tasks.list({"project_id": project_id})}

