from apollo.db.repositories.base_repository import BaseRepository


class MemoryPolicyRepository(BaseRepository):
    table = "memory_policies"
    id_prefix = "mem_policy"
    json_fields = ("scopes", "rules", "metadata")
    allowed_fields = ("name", "scopes", "retrieval_limit", "include_summaries", "include_graph", "include_files", "rules", "metadata")

