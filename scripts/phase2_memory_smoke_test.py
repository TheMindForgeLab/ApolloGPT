from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apollo.memory.memory_manager import MemoryManager
from apollo.settings import settings


def main() -> None:
    manager = MemoryManager(settings.storage_dir)
    ids = manager.ingest_text(
        "ApolloGPT Phase 2 memory stores scoped chunks for businesses, departments, projects, agents, and tasks. "
        "The context packet should retrieve relevant memory with scores and source metadata.",
        project="Phase2Memory",
        source="phase2_smoke_test",
        memory_type="test",
    )
    assert ids
    bundle = manager.retrieve_relevant("scoped chunks context packet source metadata", project="Phase2Memory", limit=5)
    assert bundle["memories"]
    top = bundle["memories"][0]
    assert top.metadata.get("retrieval_score") is not None
    print("Phase 2 memory smoke test passed.")
    print(f"Indexed chunks: {len(ids)}")
    print(f"Top memory: {top.id}")
    print(f"Score: {top.metadata.get('retrieval_score')}")


if __name__ == "__main__":
    main()

