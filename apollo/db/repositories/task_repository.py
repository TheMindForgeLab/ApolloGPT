from apollo.db.repositories.base_repository import BaseRepository


class TaskRepository(BaseRepository):
    table = "tasks"
    id_prefix = "task"
    json_fields = ("metadata",)
    allowed_fields = (
        "business_id",
        "department_id",
        "project_id",
        "agent_id",
        "title",
        "description",
        "status",
        "priority",
        "progress",
        "output_ref",
        "metadata",
    )
