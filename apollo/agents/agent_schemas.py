from dataclasses import dataclass, field


@dataclass
class AgentProfile:
    id: str
    name: str
    role: str
    tools: list[str] = field(default_factory=list)
    memory_access: list[str] = field(default_factory=list)
    autonomy_level: int = 1

