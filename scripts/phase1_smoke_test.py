from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apollo.businesses.business_manager import BusinessManager
from apollo.db.database import init_db
from apollo.db.repositories.task_repository import TaskRepository


def main() -> None:
    init_db()
    manager = BusinessManager()
    result = manager.create_business({
        "name": "Phase 1 Test Business",
        "business_type": "Test",
        "purpose": "Verify ApolloGPT Phase 1 persistence and generated structure.",
        "goals": ["Create business", "Generate starter structure"],
        "generate_starter": True,
    })
    assert result["business"]["id"]
    assert len(result["departments"]) >= 5
    assert len(result["agents"]) >= 5
    assert len(result["projects"]) == 1
    assert len(result["tasks"]) >= 2

    tasks = TaskRepository().list({"business_id": result["business"]["id"]})
    assert tasks

    print("Phase 1 smoke test passed.")
    print(f"Business: {result['business']['name']}")
    print(f"Departments: {len(result['departments'])}")
    print(f"Agents: {len(result['agents'])}")
    print(f"Projects: {len(result['projects'])}")
    print(f"Tasks: {len(tasks)}")


if __name__ == "__main__":
    main()

