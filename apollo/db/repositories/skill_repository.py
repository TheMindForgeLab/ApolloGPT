from apollo.db.repositories.base_repository import BaseRepository


class SkillRepository(BaseRepository):
    table = "skills"
    id_prefix = "skill"
    json_fields = ("tools", "input_types", "output_types", "metadata")
    allowed_fields = ("name", "description", "skill_type", "instructions", "tools", "input_types", "output_types", "metadata")

