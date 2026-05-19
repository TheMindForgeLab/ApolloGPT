from dataclasses import dataclass


@dataclass
class ModelSource:
    id: str
    provider: str
    model: str
    role: str

