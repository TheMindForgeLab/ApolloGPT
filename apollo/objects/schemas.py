from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from apollo.schemas import new_id, utc_now


@dataclass
class ApolloObject:
    object_type: str
    name: str
    workspace_id: str = "workspace_apollo"
    project_id: Optional[str] = None
    content: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: new_id("obj"))
    created_at: str = field(default_factory=utc_now)
    updated_at: str = field(default_factory=utc_now)

