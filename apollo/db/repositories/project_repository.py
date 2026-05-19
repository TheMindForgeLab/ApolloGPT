from apollo.db.repositories.base_repository import BaseRepository


class ProjectRepository(BaseRepository):
    table = "projects"
    id_prefix = "proj"
    json_fields = ("metadata",)
    allowed_fields = ("business_id", "department_id", "name", "goal", "status", "progress", "metadata")
