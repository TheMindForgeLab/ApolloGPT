from __future__ import annotations

from pathlib import Path

from apollo.objects.registry import ObjectRegistry
from apollo.objects.schemas import ApolloObject


class ObjectService:
    def __init__(self, storage_dir: Path):
        self.registry = ObjectRegistry(storage_dir)

    def create_project(self, name: str, goal: str = "") -> str:
        obj = ApolloObject(object_type="project", name=name, project_id=name, content=goal)
        return self.registry.save(obj)

    def create_task(self, name: str, project_id: str, instruction: str) -> str:
        obj = ApolloObject(object_type="task", name=name, project_id=project_id, content=instruction)
        return self.registry.save(obj)

