from __future__ import annotations

from fastapi import APIRouter, HTTPException

from apollo.db.repositories.task_repository import TaskRepository

router = APIRouter(prefix="/api/tasks", tags=["tasks"])
repository = TaskRepository()


@router.get("")
def list_tasks(
    business_id: str | None = None,
    department_id: str | None = None,
    project_id: str | None = None,
    agent_id: str | None = None,
    status: str | None = None,
):
    return {
        "items": repository.list({
            "business_id": business_id,
            "department_id": department_id,
            "project_id": project_id,
            "agent_id": agent_id,
            "status": status,
        })
    }


@router.post("")
def create_task(payload: dict):
    if not payload.get("title"):
        raise HTTPException(status_code=400, detail="Task title is required.")
    return {"task": repository.create(payload)}


@router.patch("/{task_id}")
def update_task(task_id: str, payload: dict):
    task = repository.update(task_id, payload)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return {"task": task}
