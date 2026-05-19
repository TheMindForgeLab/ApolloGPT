from apollo.db.repositories.base_repository import BaseRepository


class AutomationRepository(BaseRepository):
    table = "automations"
    id_prefix = "auto"
    json_fields = ("trigger", "conditions", "metadata")
    allowed_fields = (
        "business_id",
        "department_id",
        "project_id",
        "name",
        "trigger",
        "conditions",
        "workflow_name",
        "approval_required",
        "status",
        "metadata",
    )

