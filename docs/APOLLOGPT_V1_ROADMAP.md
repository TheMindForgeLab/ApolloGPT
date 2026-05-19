# ApolloGPT Version 1.0 Roadmap

The build path is:

1. Core Brain
2. Memory System
3. Agent System
4. Department + Business Layer
5. Model Fabric
6. Workflow + n8n Engine
7. UI Command Center
8. Media + Voice Tools
9. Research Mode
10. Distributed Node System
11. Evaluation + Security + Production

## Phase 1: Core Brain

Goal: make the backend loop reliable.

Files:

- `apollo/app.py`
- `apollo/settings.py`
- `apollo/dependencies.py`
- `apollo/core/orchestrator.py`
- `apollo/core/task_router.py`
- `apollo/core/planner.py`
- `apollo/core/execution_controller.py`
- `apollo/core/state_manager.py`
- `apollo/core/event_bus.py`
- `apollo/core/logger.py`
- `apollo/core/validator.py`
- `apollo/core/schemas.py`

Phase 1 implementation target:

- SQLite persistence in `storage/apollo.sqlite3`
- create/list/get businesses
- create/list/get departments
- create/list/get projects
- create/list agents
- create/list/update tasks
- generated starter structure when creating a business
- frontend creation studio calls the backend
- business dashboard and task board read real API data

Run:

```powershell
python scripts/phase1_smoke_test.py
```

## Phase 2: Memory System

Goal: persistent project memory with context packets.

Start with JSONL and summaries. Then upgrade `vector_store.py` to Chroma/Qdrant and `graph_store.py` to NetworkX/Neo4j.

Phase 2 implementation target:

- chunk text into scoped memory units
- ingest text/markdown-like files into local memory
- store source metadata and content hashes
- retrieve memory with project scope and retrieval scores
- expose memory search and text ingestion through API
- keep generated vector/runtime memory out of GitHub

Run:

```powershell
python scripts/phase2_memory_smoke_test.py
python scripts/ingest_text_file.py docs/APOLLOGPT_BUILD_SPEC.md --project ApolloGPT
```

## Phase 3: Agent System

Goal: manager, researcher, writer, editor, coder, media, automation, validator, analyst, and planner agents.

Agents should receive context packets and models. They should not directly own every subsystem.

## Phase 4: Business + Department Layer

Goal: structure ApolloGPT around workspaces/businesses, departments, projects, agents, tasks, and memory scopes.

## Phase 5: Model Fabric

Goal: support Ollama, LM Studio, vLLM, Text Generation WebUI, KoboldCPP, LocalAI, cloud APIs, LoRAs, MoE models, embeddings, Whisper, TTS, and Stable Diffusion/SDXL through adapters.

## Phase 6: Workflow + n8n Engine

Goal: run multi-step workflows, schedules, retries, webhook triggers, and approval-gated external actions.

## Phase 7: UI Command Center

Goal: build the 3-panel UI:

- Left: businesses, departments, projects, agents, workflows, memory, files, models, nodes.
- Center: chat, documents, workflow builder, media studio, task board, output viewer.
- Right: context packet, retrieved memory, active agents, model/node, workflow state, logs, next actions.

## Phase 8: Media + Voice

Goal: integrate Stable Diffusion/SDXL/ComfyUI, ControlNet, LoRAs, Whisper, and TTS.

## Phase 9: Research Mode

Goal: source gathering, ranking, extraction, citation, synthesis, and fact checking.

## Phase 10: Distributed Nodes

Goal: run models and jobs across multiple local machines and optional cloud nodes.

## Phase 11: Evaluation + Security + Production

Goal: auth, permissions, API keys, encryption, rate limits, model/agent/workflow evaluation, logs, backups, and deployment.
