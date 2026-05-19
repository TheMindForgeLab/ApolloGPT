from apollo.bootstrap import build_orchestrator
from apollo.schemas import UserTask


def test_core_loop_returns_output():
    orchestrator = build_orchestrator()
    result = orchestrator.run_task(UserTask(input_text="Plan ApolloGPT memory", project="TestApollo"))
    assert result.output

