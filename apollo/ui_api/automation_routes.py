from __future__ import annotations

from fastapi import APIRouter, HTTPException

from apollo.automations.automation_manager import AutomationManager

router = APIRouter(prefix="/api/automations", tags=["automations"])
manager = AutomationManager()


@router.get("")
def list_automations(
    business_id: str | None = None,
    department_id: str | None = None,
    project_id: str | None = None,
    status: str | None = None,
):
    return {
        "items": manager.list({
            "business_id": business_id,
            "department_id": department_id,
            "project_id": project_id,
            "status": status,
        })
    }


@router.post("")
def create_automation(payload: dict):
    if not payload.get("name"):
        raise HTTPException(status_code=400, detail="Automation name is required.")
    return {"automation": manager.create(payload)}
