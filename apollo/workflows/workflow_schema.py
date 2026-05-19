from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class WorkflowStep:
    name: str
    instruction: str
    project: Optional[str] = None
    metadata: Dict = field(default_factory=dict)


@dataclass
class Workflow:
    name: str
    steps: List[WorkflowStep]
    metadata: Dict = field(default_factory=dict)

