from dataclasses import dataclass, field


@dataclass
class AgentProfile:
    id: str
    name: str
    role: str
    tools: list[str] = field(default_factory=list)
    memory_access: list[str] = field(default_factory=list)
    autonomy_level: int = 1


@dataclass
class PersonaProfile:
    name: str
    tone: str = ""
    rules: list[str] = field(default_factory=list)
    examples: list[str] = field(default_factory=list)


@dataclass
class SkillProfile:
    name: str
    description: str = ""
    instructions: str = ""
    tools: list[str] = field(default_factory=list)


@dataclass
class LoRAProfile:
    name: str
    lora_type: str = "text"
    trigger_phrase: str = ""
    strength: float = 1.0
    allowed_models: list[str] = field(default_factory=list)


@dataclass
class MemoryPolicy:
    name: str
    scopes: list[str] = field(default_factory=lambda: ["project", "agent"])
    retrieval_limit: int = 8
    rules: list[str] = field(default_factory=list)
