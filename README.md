# ApolloGPT Backend Scaffold

ApolloGPT is a local-first, memory-centric, multi-agent AI operating system. This repo starts the real backend loop:

```text
Input -> Route -> Retrieve Memory -> Build Context Packet -> Select Agent
-> Select Model -> Execute -> Validate -> Store -> Improve
```

The scaffold is intentionally advanced-shaped but MVP-runnable. It can run with no cloud services, uses local JSON/JSONL storage by default, and can call Ollama when it is available.

## Quick Start

```powershell
python -m apollo.main "Write a short summary of what ApolloGPT is."
```

Run with Ollama if you have it installed:

```powershell
$env:APOLLO_USE_OLLAMA="true"
$env:APOLLO_DEFAULT_MODEL="mistral"
python -m apollo.main "Plan the ApolloGPT memory system."
```

Use LM Studio server mode:

```powershell
$env:APOLLO_MODEL_PROVIDER="lmstudio"
$env:APOLLO_LMSTUDIO_BASE_URL="http://localhost:1234/v1"
$env:APOLLO_DEFAULT_MODEL="the-model-id-loaded-in-lm-studio"
python -m apollo.main "Use the loaded local model through LM Studio."
```

Optional API server:

```powershell
pip install -r requirements.txt
uvicorn apollo.app:app --reload --port 8000
```

See [docs/SETUP_ADVANCED.md](./docs/SETUP_ADVANCED.md) for the full setup path.
See [docs/MODEL_SOURCES_AND_INTERFACE_PLAN.md](./docs/MODEL_SOURCES_AND_INTERFACE_PLAN.md) for Ollama, LM Studio, vLLM, Text Generation WebUI, KoboldCPP, LocalAI, MoE routing, and the model-router UI plan.

## Project Guides

- [Build Spec](./docs/APOLLOGPT_BUILD_SPEC.md)
- [V1 Roadmap](./docs/APOLLOGPT_V1_ROADMAP.md)
- [UI Blueprint](./docs/APOLLOGPT_UI_BLUEPRINT.md)
- [Model Sources and Interface Plan](./docs/MODEL_SOURCES_AND_INTERFACE_PLAN.md)
