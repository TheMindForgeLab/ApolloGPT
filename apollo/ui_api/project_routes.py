from __future__ import annotations

from fastapi import APIRouter, HTTPException

from apollo.db.repositories.project_repository import ProjectRepository
from apollo.projects import ProjectManager

router = APIRouter(prefix="/api/projects", tags=["projects"])
manager = ProjectManager()
repository = ProjectRepository()


@router.get("")
def list_projects(business_id: str | None = None, department_id: str | None = None):
    return {"items": repository.list({"business_id": business_id, "department_id": department_id})}


@router.post("")
def create_project(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Project name is required.")
    return manager.create_project(payload)


@router.get("/{project_id}")
def get_project(project_id: str):
    dashboard = manager.dashboard(project_id)
    if not dashboard:
        raise HTTPException(status_code=404, detail="Project not found.")
    return dashboard
