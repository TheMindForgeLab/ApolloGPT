# ApolloGPT Model Sources and Interface Plan

ApolloGPT should be model-source agnostic. Ollama is only one backend. The system should route through a common adapter layer so the UI can choose a model source, model, LoRA/adapter profile, precision policy, and execution node without rewriting the rest of the app.

## Local Model Sources To Support

### Ollama

Best for:

- simple local setup
- quick testing
- common models like Mistral, Llama, DeepSeek, Qwen, Phi
- API-first usage from Python

Tradeoff:

- less control over advanced LoRA, quantization, and model-loading details than specialized runners

ApolloGPT provider:

```powershell
$env:APOLLO_MODEL_PROVIDER="ollama"
$env:APOLLO_DEFAULT_MODEL="mistral"
```

### LM Studio

Best for:

- GGUF models
- easy manual model loading
- OpenAI-compatible local server
- trying many models quickly
- MoE models that only activate part of their parameters

LM Studio usually serves at:

```text
http://localhost:1234/v1
```

ApolloGPT provider:

```powershell
$env:APOLLO_MODEL_PROVIDER="lmstudio"
$env:APOLLO_LMSTUDIO_BASE_URL="http://localhost:1234/v1"
$env:APOLLO_DEFAULT_MODEL="the-model-id-shown-in-lm-studio"
```

### vLLM

Best for:

- high-throughput GPU serving
- serious local/server deployments
- OpenAI-compatible API
- batching and concurrent users

Tradeoff:

- setup is more technical and hardware dependent

ApolloGPT provider:

```powershell
$env:APOLLO_MODEL_PROVIDER="vllm"
$env:APOLLO_VLLM_BASE_URL="http://localhost:8001/v1"
```

### Text Generation WebUI

Best for:

- advanced model experimentation
- GPTQ, EXL2, GGUF, LoRA workflows
- manual model and adapter control
- power-user local AI setups

ApolloGPT provider:

```powershell
$env:APOLLO_MODEL_PROVIDER="textgen-webui"
$env:APOLLO_TEXTGEN_BASE_URL="http://localhost:5000"
```

### KoboldCPP

Best for:

- GGUF models
- CPU/GPU split
- simple local inference server
- running models on limited hardware

ApolloGPT provider:

```powershell
$env:APOLLO_MODEL_PROVIDER="koboldcpp"
$env:APOLLO_KOBOLDCPP_BASE_URL="http://localhost:5001"
```

### LocalAI

Best for:

- self-hosted OpenAI-compatible stack
- multiple model types behind one API
- text, embeddings, audio, and image pipelines depending on setup

ApolloGPT provider:

```powershell
$env:APOLLO_MODEL_PROVIDER="localai"
$env:APOLLO_LOCALAI_BASE_URL="http://localhost:8080/v1"
```

## MoE Models

MoE means mixture of experts. A model can have a large total parameter count but activate only part of it per token. This is why a model might be described as something like 35B total but only a smaller active parameter count during inference.

Why ApolloGPT should care:

- MoE can give stronger capability without paying the full runtime cost every token.
- It fits ApolloGPT's philosophy: route work to the right expert instead of forcing one dense model to do everything.
- The UI should show both total size and active parameters when known.

Recommended ApolloGPT handling:

- Store `size` and `active_parameters` in the model registry.
- Route MoE models toward reasoning, planning, writing, and synthesis when they benchmark well.
- Keep smaller dense models for quick classification, tagging, summarization, and routing.
- Let the user pin a preferred MoE model for “power mode.”

## Interface Needed

The UI should have a Tools & Models or Model Router panel with:

- provider selector: Ollama, LM Studio, vLLM, TextGen WebUI, KoboldCPP, LocalAI, Cloud
- model selector
- role mapping: default, writing, reasoning, coding, embedding, image, voice
- mode selector: auto, manual, compare
- LoRA/adapter selector
- quantization/precision display
- context window display
- total parameters and active parameters
- local endpoint health
- “why this model was selected” trace

## Backend Contract

Every model source should obey:

```python
model.generate(prompt: str) -> str
```

That keeps agents, memory, workflows, and UI independent from the model runner.

## Best Near-Term Path

1. Keep Ollama for simple local models.
2. Add LM Studio for trying many GGUF and MoE models.
3. Add Text Generation WebUI when you want heavier LoRA/QLoRA experimentation.
4. Add vLLM when you want a more serious always-on model server.
5. Add Stable Diffusion/ComfyUI as a separate media adapter instead of mixing it into the text model router.

