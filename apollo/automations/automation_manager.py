from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


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

    def register(self, automation: Automation) -> None:
        self.automations[automation.name] = automation

