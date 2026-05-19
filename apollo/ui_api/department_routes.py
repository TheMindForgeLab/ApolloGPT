from __future__ import annotations

from fastapi import APIRouter, HTTPException

from apollo.db.repositories.department_repository import DepartmentRepository
from apollo.departments.department_manager import DepartmentManager

router = APIRouter(prefix="/api/departments", tags=["departments"])
manager = DepartmentManager()
repository = DepartmentRepository()


@router.get("")
def list_departments(business_id: str | None = None):
    return {"items": repository.list({"business_id": business_id})}


@router.post("")
def create_department(payload: dict):
    if not payload.get("business_id") or not payload.get("name"):
        raise HTTPException(status_code=400, detail="business_id and name are required.")
    return manager.create_department(payload)


@router.get("/{department_id}")
def get_department(department_id: str):
    dashboard = manager.dashboard(department_id)
    if not dashboard:
        raise HTTPException(status_code=404, detail="Department not found.")
    return dashboard
