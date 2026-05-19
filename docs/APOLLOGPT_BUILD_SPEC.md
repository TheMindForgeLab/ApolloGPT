# ApolloGPT Build Spec

ApolloGPT is a memory-centric, multi-agent AI operating system. The product is not a chatbot with tools attached; it is a permanent operating loop that understands a task, retrieves memory, structures context, routes work to agents and models, validates the result, stores what happened, and improves over time.

## Core Loop

```text
User Input
  -> Orchestrator
  -> Task Router
  -> Memory Manager
  -> Context Packet Builder
  -> Agent Controller
  -> Model Router
  -> Tool / Workflow Engine
  -> Validator
  -> Memory Update
  -> Final Output
```

The orchestrator coordinates. It should not absorb every responsibility. Memory, agents, models, tools, validation, logging, workflows, and UI/API access all remain separate modules.

## MVP Goal

The first working backend should be able to:

1. Take a user message.
2. Classify the task.
3. Retrieve relevant memory.
4. Build a context packet.
5. Pick an agent.
6. Pick a local model.
7. Generate a response.
8. Save the conversation.
9. Add the output to memory.
10. Use that memory in the next response.

The first version should prioritize a real running loop over the full dream architecture.

## MVP Project Structure

```text
apollo_mvp/
|-- main.py
|-- config.py
|-- schemas.py
|
|-- core/
|   |-- orchestrator.py
|   |-- task_router.py
|   |-- context_packet_builder.py
|   |-- validator.py
|
|-- agents/
|   |-- agent_base.py
|   |-- agent_controller.py
|   |-- writer_agent.py
|   |-- coder_agent.py
|
|-- models/
|   |-- model_router.py
|   |-- model_base.py
|   |-- ollama_adapter.py
|
|-- memory/
|   |-- memory_manager.py
|   |-- raw_store.py
|   |-- vector_store.py
|   |-- summary_manager.py
|
|-- data/
    |-- raw/
    |-- summaries/
    |-- vector_db/
```

## Full Target Project Structure

```text
apollo_system/
|-- main.py
|-- config.py
|-- schemas.py
|-- database.py
|
|-- core/
|   |-- orchestrator.py
|   |-- task_router.py
|   |-- context_packet_builder.py
|   |-- validator.py
|   |-- logger.py
|   |-- state_manager.py
|
|-- agents/
|   |-- agent_base.py
|   |-- agent_controller.py
|   |-- research_agent.py
|   |-- writer_agent.py
|   |-- coder_agent.py
|   |-- strategist_agent.py
|   |-- automation_agent.py
|   |-- project_manager_agent.py
|
|-- models/
|   |-- model_router.py
|   |-- model_base.py
|   |-- ollama_adapter.py
|   |-- lmstudio_adapter.py
|   |-- openai_adapter.py
|   |-- embedding_model.py
|
|-- memory/
|   |-- memory_manager.py
|   |-- raw_store.py
|   |-- vector_store.py
|   |-- graph_store.py
|   |-- summary_manager.py
|   |-- working_memory.py
|   |-- procedural_memory.py
|   |-- preference_memory.py
|   |-- outcome_memory.py
|
|-- workflows/
|   |-- workflow_engine.py
|   |-- workflow_registry.py
|   |-- workflow_step.py
|   |-- templates/
|       |-- content_workflow.py
|       |-- research_workflow.py
|       |-- coding_workflow.py
|
|-- tools/
|   |-- tool_registry.py
|   |-- file_tools.py
|   |-- web_tools.py
|   |-- code_tools.py
|   |-- document_tools.py
|   |-- api_tools.py
|
|-- ingestion/
|   |-- file_ingestor.py
|   |-- text_chunker.py
|   |-- metadata_extractor.py
|   |-- memory_ingestor.py
|
|-- api/
|   |-- api_server.py
|   |-- chat_routes.py
|   |-- memory_routes.py
|   |-- agent_routes.py
|   |-- project_routes.py
|   |-- workflow_routes.py
|
|-- data/
    |-- raw/
    |-- logs/
    |-- summaries/
    |-- vector_db/
    |-- graph_db/
```

## Shared Schemas

All modules should communicate through shared typed objects. Start with Pydantic models:

```python
from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class UserTask(BaseModel):
    input_text: str
    project: Optional[str] = None
    goal: Optional[str] = None
    priority: str = "normal"


class TaskAnalysis(BaseModel):
    task_type: str
    required_agent: str
    required_model: str
    required_tools: List[str]
    project: Optional[str]
    complexity: str


class MemoryItem(BaseModel):
    id: str
    content: str
    memory_type: str
    project: Optional[str]
    importance: str
    metadata: Dict[str, Any]


class ContextPacket(BaseModel):
    task: UserTask
    task_analysis: TaskAnalysis
    agent_role: str
    relevant_memories: List[MemoryItem]
    project_context: Optional[str]
    user_preferences: Dict[str, Any]
    constraints: List[str]
    output_format: Optional[str]


class AgentResult(BaseModel):
    output: str
    reasoning_summary: Optional[str]
    tool_calls: List[Dict[str, Any]]
    memories_to_store: List[MemoryItem]
    success: bool
```

## Core Module Contracts

### Orchestrator

Responsibilities:

- Accept a `UserTask`.
- Ask the task router for a `TaskAnalysis`.
- Retrieve memories through the memory manager.
- Build a `ContextPacket`.
- Select an agent.
- Select a model.
- Run the agent.
- Validate the result.
- Store the interaction and learned memory.
- Return the final output.

The orchestrator coordinates the loop, but it does not directly implement memory storage, model calls, or agent behavior.

### Task Router

Responsibilities:

- Classify task type.
- Choose required agent.
- Choose model category.
- List required tools.
- Estimate complexity.
- Preserve project context.

Start with keyword rules. Later, route with a small local model.

### Memory Manager

Responsibilities:

- Retrieve relevant memory from all active memory layers.
- Store raw interactions.
- Add searchable vector memories.
- Update summaries.
- Store outcomes and validation results.
- Later, update graph relationships.

The memory manager coordinates memory. Agents should receive memory through context packets rather than reaching into stores directly.

### Context Packet Builder

Responsibilities:

- Turn raw retrieved memory into a clean task brief.
- Include only relevant memories.
- Add project context, preferences, constraints, current state, expected output, and available tools.

This is one of ApolloGPT's defining pieces. Basic RAG retrieves information; ApolloGPT constructs usable context.

### Agent Controller

Responsibilities:

- Select the right agent from a registry.
- Fall back to the project manager agent when unsure.
- Later, coordinate multiple agents for complex tasks.

### Model Router

Responsibilities:

- Select local-first models by task type, complexity, cost, speed, privacy, and capability.
- Route coding tasks to coding models.
- Route writing tasks to writing models.
- Route reasoning tasks to stronger reasoning models.
- Use cloud fallback only when configured.

Every model provider should be hidden behind a common adapter interface.

### Validator

Responsibilities:

- Check that output is not empty.
- Check requested format when possible.
- Check whether tool calls succeeded.
- Check whether the response appears to answer the task.
- Later, add fact-checking, tests, schema validation, security review, and hallucination checks.

### Logger

Responsibilities:

- Write a trace for every task.
- Record task id, user input, analysis, memory used, agent, model, tools, output, validation, stored memory ids, and timestamp.

Logs are future training material for the system's improvement loop.

## Memory Layers

### Raw Memory

Stores full conversations, logs, files, and outputs. Use JSON files first, then SQLite or PostgreSQL later.

### Vector Memory

Stores embeddings for semantic search. Start with ChromaDB or a simple local substitute; later support Qdrant or FAISS.

### Graph Memory

Stores relationships between users, projects, agents, files, tools, tasks, outputs, and decisions. Start with JSON; later move to Neo4j or another graph database.

### Summary Memory

Maintains compressed summaries for projects, conversations, agents, workflows, and decisions.

### Working Memory

Tracks current session, project, task, agent, goal, constraints, and recent messages.

### Procedural Memory

Stores reusable processes such as writing articles, running research, building modules, creating campaigns, or generating posts.

### Preference Memory

Stores user preferences for format, style, continuity, detail level, architecture choices, and working habits.

### Outcome Memory

Stores what worked, what failed, what feedback was given, and how future attempts should improve.

## Agents

All agents inherit from `AgentBase` and follow one shape:

- Receive a `ContextPacket`.
- Build a prompt.
- Use a model adapter.
- Return an `AgentResult`.

Initial agents:

- Writer Agent: articles, posts, scripts, long-form content.
- Coder Agent: code, architecture, debugging, repo planning.
- Project Manager Agent: task breakdown, planning, coordination.

Later agents:

- Research Agent
- Strategist Agent
- Automation Agent
- Validator Agent
- Domain-specific custom agents

Agents should not talk directly to every subsystem. They execute against the context and model they are given.

## Model Adapters

Every model backend should expose the same interface:

```python
class ModelBase:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
```

Initial adapter:

- Ollama adapter

Later adapters:

- LM Studio adapter
- OpenAI/cloud adapter
- llama.cpp adapter
- Embedding model adapter

## Workflow Engine

Start with linear workflows:

```text
Research topic -> Summarize findings -> Write article -> Validate article -> Store final output
```

Later, workflows can become DAGs with branching, approval gates, retries, scheduling, and event-driven execution.

## Tool Registry

The tool registry owns callable system tools:

- Read file
- Write file
- Search memory
- Summarize document
- Run Python
- Call API
- Create document
- Send webhook
- Connect to n8n

Agents should request tools through the registry rather than directly importing tool implementations.

## Database Progression

MVP:

- JSON for raw logs and summaries
- SQLite for structured records
- ChromaDB or local vector store for embeddings
- Local folders for raw artifacts

Advanced:

- PostgreSQL for structured state
- Qdrant for vector memory
- Neo4j for graph memory
- Redis/Celery for queues
- MinIO or S3-compatible storage for files

## Build Phases

### Phase 1: Basic System Loop

Files:

- `main.py`
- `schemas.py`
- `config.py`
- `core/orchestrator.py`
- `core/task_router.py`
- `models/ollama_adapter.py`
- `models/model_router.py`
- `agents/agent_base.py`
- `agents/writer_agent.py`
- `agents/agent_controller.py`
- `memory/raw_store.py`
- `memory/memory_manager.py`
- `core/context_packet_builder.py`

Goal:

User types input, the system routes the task, an agent responds using a local model, and the output is saved.

### Phase 2: Vector Memory

Files:

- `memory/vector_store.py`
- `models/embedding_model.py`
- `ingestion/memory_ingestor.py`
- `ingestion/text_chunker.py`

Goal:

The system retrieves relevant past memory before answering.

### Phase 3: Project Memory

Files:

- `projects/project_manager.py`
- `projects/project_store.py`
- `memory/summary_manager.py`

Goal:

Every memory can belong to a project.

### Phase 4: More Agents

Files:

- `agents/research_agent.py`
- `agents/coder_agent.py`
- `agents/strategist_agent.py`
- `agents/automation_agent.py`
- `agents/validator_agent.py`

Goal:

Different tasks route to different specialized agents.

### Phase 5: Workflow Engine

Files:

- `workflows/workflow_engine.py`
- `workflows/workflow_registry.py`
- `workflows/workflow_step.py`

Goal:

The system can run multi-step processes.

### Phase 6: Graph Memory

Files:

- `memory/graph_store.py`
- `ingestion/entity_extractor.py`
- `ingestion/relationship_extractor.py`

Goal:

The system understands relationships between projects, agents, files, people, and tasks.

### Phase 7: API and UI

Files:

- `api/api_server.py`
- `api/chat_routes.py`
- `api/memory_routes.py`
- `api/agent_routes.py`
- `api/project_routes.py`
- `api/workflow_routes.py`

Goal:

A frontend can talk to the backend.

## Design Rules

1. Every task becomes a structured object.
2. Every agent receives a context packet.
3. Every model is accessed through an adapter.
4. Every memory write includes metadata.
5. Every output gets logged.
6. Every workflow is made of steps.
7. Every module has one job.
8. Agents do not directly own memory, routing, logging, or workflow orchestration.
9. The system starts local-first and uses cloud fallback only when configured.
10. The loop is the product.

