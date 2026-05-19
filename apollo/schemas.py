from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from uuid import uuid4


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:12]}"


@dataclass
class UserTask:
    input_text: str
    project: Optional[str] = "ApolloGPT"
    goal: Optional[str] = None
    priority: str = "normal"
    metadata: Dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: new_id("task"))
    created_at: str = field(default_factory=utc_now)


@dataclass
class TaskAnalysis:
    task_type: str
    required_agent: str
    required_model: str
    required_tools: List[str]
    project: Optional[str]
    complexity: str
    intent: str = "general"
    privacy_level: str = "local"
    modality: str = "text"


@dataclass
class MemoryItem:
    id: str
    content: str
    memory_type: str
    project: Optional[str]
    importance: float = 0.5
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now)


@dataclass
class ContextPacket:
    packet_id: str
    task: UserTask
    task_analysis: TaskAnalysis
    agent_role: str
    relevant_memories: List[MemoryItem]
    project_context: Optional[str]
    user_preferences: Dict[str, Any]
    constraints: List[str]
    tools_available: List[str]
    workflow_state: Dict[str, Any] = field(default_factory=dict)
    output_format: Optional[str] = "markdown"


@dataclass
class AgentResult:
    output: str
    reasoning_summary: Optional[str]
    tool_calls: List[Dict[str, Any]]
    memories_to_store: List[MemoryItem]
    success: bool
    agent_id: str
    model_id: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ValidationResult:
    output: str
    success: bool
    issues: List[str]
    score: float
    raw_result: AgentResult


def to_dict(value: Any) -> Dict[str, Any]:
    return asdict(value)

