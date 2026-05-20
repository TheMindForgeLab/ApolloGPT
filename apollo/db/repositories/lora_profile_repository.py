from apollo.db.repositories.base_repository import BaseRepository


class LoRAProfileRepository(BaseRepository):
    table = "lora_profiles"
    id_prefix = "lora"
    json_fields = ("allowed_models", "metadata")
    allowed_fields = ("name", "lora_type", "base_model", "trigger_phrase", "strength", "adapter_path", "allowed_models", "metadata")

