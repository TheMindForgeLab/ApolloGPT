"use client";

import { FormEvent, useState } from "react";
import { createCustomAgent, createLoRAProfile, createMemoryPolicy, createPersona, createSkill } from "../../lib/api";

export default function AgentIntelligenceWizard() {
  const [status, setStatus] = useState("");
  const [agentName, setAgentName] = useState("Adaptive Writer Agent");
  const [personaName, setPersonaName] = useState("Programmable Writer Persona");
  const [tone, setTone] = useState("clear, memory-aware, practical, adaptable");
  const [skillName, setSkillName] = useState("Longform Writing");
  const [loraName, setLoraName] = useState("Optional Text Style Adapter");

  async function submit(event: FormEvent) {
    event.preventDefault();
    setStatus("Creating persona, skill, LoRA profile, memory policy, and agent...");
    try {
      const persona = await createPersona({
        name: personaName,
        tone,
        description: "A reusable writing/personality layer that can carry across many LLMs.",
        rules: ["Use project memory", "Match the selected style", "Keep outputs useful and structured"]
      });
      const skill = await createSkill({
        name: skillName,
        skill_type: "writing",
        description: "Writes long-form content using memory, examples, and style constraints.",
        instructions: "Retrieve project, business, and agent memory before drafting. Preserve style and revise with feedback.",
        tools: ["memory_search", "file_system", "document_builder"]
      });
      const lora = await createLoRAProfile({
        name: loraName,
        lora_type: "text",
        base_model: "any-compatible-local-model",
        trigger_phrase: "",
        strength: 0.8,
        allowed_models: ["ollama", "lmstudio", "vllm", "textgen-webui"]
      });
      const memoryPolicy = await createMemoryPolicy({
        name: `${agentName} Memory Policy`,
        scopes: ["business", "department", "project", "agent"],
        retrieval_limit: 12,
        rules: ["Prefer agent examples", "Include brand voice", "Include project decisions"]
      });
      const agent = await createCustomAgent({
        name: agentName,
        agent_type: "writer",
        role: "Writes with programmable persona, style, memory, skills, and optional LoRA adapters.",
        preferred_model: "auto",
        memory_access: ["business", "department", "project", "agent"],
        tool_access: ["memory_search", "file_system", "document_builder"],
        workflow_permissions: ["draft", "revise", "handoff", "request_approval"],
        persona_id: persona.persona.id,
        skill_ids: [skill.skill.id],
        lora_profile_ids: [lora.lora.id],
        memory_policy_id: memoryPolicy.memory_policy.id,
        style_profile: {
          tone,
          format: "structured markdown",
          portability: "works across multiple LLM providers"
        }
      });
      setStatus(`Created ${agent.agent.name}. Prompt composition is ready.`);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Failed to create agent intelligence profile.");
    }
  }

  return (
    <section className="card">
      <div className="section-title">Agent Intelligence Wizard</div>
      <h3 style={{ marginTop: 0 }}>Create Custom Agent Stack</h3>
      <form onSubmit={submit} className="mini-list">
        <input value={agentName} onChange={(event) => setAgentName(event.target.value)} placeholder="Agent name" />
        <input value={personaName} onChange={(event) => setPersonaName(event.target.value)} placeholder="Persona name" />
        <input value={tone} onChange={(event) => setTone(event.target.value)} placeholder="Tone/style" />
        <input value={skillName} onChange={(event) => setSkillName(event.target.value)} placeholder="Skill name" />
        <input value={loraName} onChange={(event) => setLoraName(event.target.value)} placeholder="LoRA / adapter profile" />
        <button className="btn primary" type="submit">Create Agent Stack</button>
        {status && <div>{status}</div>}
      </form>
    </section>
  );
}
