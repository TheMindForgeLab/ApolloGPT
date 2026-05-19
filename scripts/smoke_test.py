from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apollo.bootstrap import build_orchestrator
from apollo.schemas import UserTask


def main() -> None:
    orchestrator = build_orchestrator()
    result = orchestrator.run_task(UserTask(input_text="Plan ApolloGPT memory next steps.", project="SmokeTest"))
    assert result.output, "Expected ApolloGPT to return output"
    print("Smoke test passed.")
    print(f"Agent: {result.raw_result.agent_id}")
    print(f"Model: {result.raw_result.model_id}")


if __name__ == "__main__":
    main()
