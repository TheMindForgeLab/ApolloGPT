# ApolloGPT UI Blueprint

ApolloGPT is not just a chat screen. It is a command center for building, operating, monitoring, and evolving a memory-centric AI business/project operating system.

The guiding layout is:

```text
LEFT   = What exists
CENTER = What is happening
RIGHT  = Why it is happening / what controls it
```

## UI Philosophy

ApolloGPT should feel like:

- ChatGPT
- Notion
- n8n
- Local AI Studio
- Project manager
- Agent command center

The product rule is:

Simple by default. Powerful when expanded.

Standard Mode exposes chat, projects, files, tasks, and simple automations. Advanced Mode exposes agent builder, department designer, workflow canvas, memory explorer, model router, LoRA manager, node monitor, knowledge graph, and automation debugger.

## Three Panels

### Left Panel: Structure

The left panel organizes businesses, departments, projects, agents, workflows, tasks, memory, files, models, LoRAs, personas, automations, nodes, and settings.

### Center Panel: Work / Creation / Execution

The center panel changes modes:

- Chat
- Workflow Builder
- Document Builder
- Project Workspace
- Task Board
- Media Studio
- Agent Team Room
- Memory Explorer

### Right Panel: Intelligence / Tools / Awareness

The right panel shows context packet, retrieved memory, active agents, workflow status, tasks, files, logs, model used, tools, node usage, and next actions.

## Main V1 Screens

1. Dashboard
2. Chat
3. Project Workspace
4. Agent Builder
5. Department Builder
6. Workflow Builder
7. Memory Viewer
8. File Ingestion
9. Task Board
10. Settings

## V2 Screens

1. Business Dashboard
2. LoRA Manager
3. Model Router
4. Node Monitor
5. Media Studio
6. Prompt Library
7. Knowledge Graph
8. Automation Logs
9. Document Builder
10. Team Room

## MVP UI Build Order

1. Skeleton Command Center: left panel, center chat, right inspector.
2. Creation Studio: create business, department, agent, project, task.
3. Memory + Files: upload, chunk, index, retrieved memory, chat summaries.
4. Workflow Builder: React Flow canvas, node palette, save workflow JSON, run simple workflow.
5. Agent Execution: configs, routing, model router, tool access, memory injection.
6. Media + Automation: Stable Diffusion, LoRA manager, Whisper, n8n, schedulers, webhooks.

## Agent Intelligence Wizard

Agent creation should be composable:

```text
Base Agent + Persona + Skill Mix + Style Profile + LoRA/Adapter Stack + Memory Policy + Model Preference
```

The first wizard implementation creates:

- persona profile
- skill profile
- LoRA profile
- memory/RAG policy
- custom agent intelligence profile
- composed prompt preview

This allows a writer style or other specialized persona to carry across multiple model providers instead of being locked to one LLM.
