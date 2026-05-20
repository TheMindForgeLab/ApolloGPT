from apollo.db.repositories.base_repository import BaseRepository


class PersonaRepository(BaseRepository):
    table = "personas"
    id_prefix = "persona"
    json_fields = ("rules", "examples", "metadata")
    allowed_fields = ("name", "description", "tone", "rules", "examples", "metadata")

