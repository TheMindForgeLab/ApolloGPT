from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict

from apollo.db.repositories.automation_repository import AutomationRepository


@dataclass
class Automation:
    name: str
    trigger: Dict
    workflow_name: str
    approval_required: bool = True
    status: str = "draft"


class AutomationManager:
    def __init__(self):
        self.automations: dict[str, Automation] = {}
        self.repository = AutomationRepository()

    def register(self, automation: Automation) -> None:
        self.automations[automation.name] = automation

    def create(self, payload: dict) -> dict:
        automation = {
            "business_id": payload.get("business_id"),
            "department_id": payload.get("department_id"),
            "project_id": payload.get("project_id"),
            "name": payload["name"],
            "trigger": payload.get("trigger", {}),
            "conditions": payload.get("conditions", []),
            "workflow_name": payload.get("workflow_name", ""),
            "approval_required": int(bool(payload.get("approval_required", True))),
            "status": payload.get("status", "draft"),
            "metadata": payload.get("metadata", {}),
        }
        return self.repository.create(automation)

    def list(self, filters: dict | None = None) -> list[dict]:
        return self.repository.list(filters or {})
