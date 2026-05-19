from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from apollo.models.model_registry import ModelRegistry
from apollo.models.model_router import ModelRouter
from apollo.schemas import TaskAnalysis
from apollo.settings import settings


def main() -> None:
    registry = ModelRegistry(settings.model_sources_path)
    providers = registry.providers()
    assert "ollama" in providers
    assert "lmstudio" in providers
    assert "textgen-webui" in providers

    analysis = TaskAnalysis(
        task_type="general",
        required_agent="manager",
        required_model="reasoning",
        required_tools=[],
        project="ApolloGPT",
        complexity="medium",
    )
    model = ModelRouter(settings).select_model(analysis)
    assert model.model_id
    print("Model provider smoke test passed.")
    print(f"Registered providers: {', '.join(providers)}")
    print(f"Selected adapter: {model.model_id}")


if __name__ == "__main__":
    main()

