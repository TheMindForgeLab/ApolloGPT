from apollo.db.repositories.base_repository import BaseRepository


class DepartmentRepository(BaseRepository):
    table = "departments"
    id_prefix = "dept"
    json_fields = ("allowed_tools", "metadata")
    allowed_fields = ("business_id", "name", "purpose", "manager_agent_id", "allowed_tools", "memory_scope", "metadata")
