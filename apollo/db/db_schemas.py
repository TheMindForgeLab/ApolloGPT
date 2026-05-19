from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class BusinessCreate:
    name: str
    business_type: str = "Custom"
    purpose: str = ""
    goals: List[str] = field(default_factory=list)
    brand_voice: str = ""
    constraints: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DepartmentCreate:
    business_id: str
    name: str
    purpose: str = ""
    manager_agent_id: Optional[str] = None
    allowed_tools: List[str] = field(default_factory=list)
    memory_scope: str = "department"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ProjectCreate:
    name: str
    business_id: Optional[str] = None
    department_id: Optional[str] = None
    goal: str = ""
    status: str = "active"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentCreate:
    name: str
    business_id: Optional[str] = None
    department_id: Optional[str] = None
    agent_type: str = "specialist"
    role: str = ""
    persona: str = ""
    preferred_model: str = ""
    fallback_model: str = ""
    memory_access: List[str] = field(default_factory=list)
    tool_access: List[str] = field(default_factory=list)
    workflow_permissions: List[str] = field(default_factory=list)
    lora_profile: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TaskCreate:
    title: str
    business_id: Optional[str] = None
    department_id: Optional[str] = None
    project_id: Optional[str] = None
    agent_id: Optional[str] = None
    description: str = ""
    status: str = "backlog"
    priority: str = "normal"
    progress: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)
