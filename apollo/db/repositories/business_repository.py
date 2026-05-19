from apollo.db.repositories.base_repository import BaseRepository


class BusinessRepository(BaseRepository):
    table = "businesses"
    id_prefix = "biz"
    json_fields = ("goals", "constraints", "metadata")
    allowed_fields = ("name", "business_type", "purpose", "goals", "brand_voice", "constraints", "metadata")
