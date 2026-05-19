# ApolloGPT Advanced Setup

This scaffold is built from the ApolloGPT documents and infographics: memory is the operating substrate, objects organize everything, agents execute work, workflows coordinate multi-step processes, model routing stays local-first, and the UI/API later exposes the whole system as a control center.

## 1. Create the Python Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The core CLI works without optional packages. `requirements.txt` is for the FastAPI server and future Chroma/NetworkX upgrades.

If Windows does not recognize `python`, install Python from python.org or the Microsoft Store, then reopen PowerShell. In this Codex workspace I verified the scaffold using the bundled runtime at:

```powershell
C:\Users\TheLi\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
```

## 2. Configure Local Models

Install Ollama and pull your preferred models:

```powershell
ollama pull mistral
ollama pull llama3
ollama pull deepseek-coder
```

Enable Ollama for ApolloGPT:

```powershell
$env:APOLLO_USE_OLLAMA="true"
$env:APOLLO_DEFAULT_MODEL="mistral"
$env:APOLLO_REASONING_MODEL="llama3"
$env:APOLLO_CODING_MODEL="deepseek-coder"
```

Without these variables, ApolloGPT uses a local placeholder adapter so the full orchestration loop still runs.

### Other Model Sources

ApolloGPT now has adapter scaffolds for:

- Ollama
- LM Studio
- vLLM
- LocalAI
- Text Generation WebUI
- KoboldCPP
- any OpenAI-compatible local server

LM Studio example:

```powershell
$env:APOLLO_MODEL_PROVIDER="lmstudio"
$env:APOLLO_LMSTUDIO_BASE_URL="http://localhost:1234/v1"
$env:APOLLO_DEFAULT_MODEL="the-model-id-loaded-in-lm-studio"
python -m apollo.main "Explain what model source is active."
```

Text Generation WebUI example:

```powershell
$env:APOLLO_MODEL_PROVIDER="textgen-webui"
$env:APOLLO_TEXTGEN_BASE_URL="http://localhost:5000"
python -m apollo.main "Run this through the loaded text-generation-webui model."
```

KoboldCPP example:

```powershell
$env:APOLLO_MODEL_PROVIDER="koboldcpp"
$env:APOLLO_KOBOLDCPP_BASE_URL="http://localhost:5001"
python -m apollo.main "Run this through KoboldCPP."
```

The longer strategy is in `MODEL_SOURCES_AND_INTERFACE_PLAN.md`.

## 3. Run the CLI Loop

```powershell
python -m apollo.main "Create a build plan for ApolloGPT project memory."
python -m apollo.main --project ApolloGPT "Write the next steps for adding vector memory."
```

No-dependency smoke test:

```powershell
python scripts/smoke_test.py
```

Each run creates local memory under `storage/`:

- `storage/raw_memory/interactions.jsonl`
- `storage/vector_db/memory_items.jsonl`
- `storage/summaries/apollogpt.md`
- `storage/graph_db/relationships.jsonl`
- `storage/logs/events.jsonl`

## 4. Run the API

```powershell
uvicorn apollo.app:app --reload --port 8000
```

Useful endpoints:

- `GET /health`
- `POST /chat`

Example:

```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:8000/chat -ContentType 'application/json' -Body '{"message":"Plan the memory system","project":"ApolloGPT"}'
```

## 5. How The Current Backend Works

The active loop is:

1. `apollo/main.py` or `apollo/app.py` receives input.
2. `TaskRouter` classifies the task.
3. `MemoryManager` retrieves lexical memory, summaries, graph links, and preferences.
4. `ContextPacketBuilder` builds a structured context packet.
5. `AgentController` picks a specialized agent.
6. `ModelRouter` chooses the local model category.
7. The agent builds a prompt and calls the model adapter.
8. `Validator` checks the output.
9. `MemoryManager` stores raw logs, searchable memory, summaries, and graph links.
10. `ApolloLogger` writes the execution trace.

## 6. Advanced Upgrade Path

Phase 1 is now scaffolded. Next implementation targets:

1. Replace lexical `VectorMemory` with ChromaDB embeddings.
2. Add SQLite object registry for workspaces, projects, departments, tasks, outputs, and files.
3. Expand `GraphMemory` with NetworkX traversal and relationship queries.
4. Add model registry metadata for local models, LoRAs, QLoRAs, Stable Diffusion, Whisper, and TTS.
5. Add workflow templates for content, research, coding, and automation.
6. Add n8n webhook execution with approval gates.
7. Add FastAPI routes for memory, agents, workflows, automations, models, and nodes.
8. Build the 3-panel UI: structure, execution, intelligence state.

## 7. Design Guardrails

- Agents receive context packets; they do not rummage through every store.
- Memory writes always include metadata.
- Model providers are hidden behind adapters.
- Workflows are made of explicit steps.
- Local-first is the default.
- Cloud fallback and external actions require deliberate configuration.
- The loop is the product.
