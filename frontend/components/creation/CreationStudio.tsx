"use client";

import { FormEvent, useState } from "react";
import { createBusiness } from "../../lib/api";

const createTypes = ["Business", "Department", "Project", "Agent", "Persona", "Workflow", "Task", "Memory Pack", "LoRA Profile", "Automation"];

export default function CreationStudio() {
  const [name, setName] = useState("New Apollo Business");
  const [purpose, setPurpose] = useState("Use ApolloGPT agents, memory, and workflows to execute real work.");
  const [status, setStatus] = useState("");

  async function submit(event: FormEvent) {
    event.preventDefault();
    setStatus("Creating business...");
    try {
      const result = await createBusiness({
        name,
        business_type: "Custom",
        purpose,
        goals: ["Create operating structure", "Generate starter agents", "Build first workflow"],
        generate_starter: true
      });
      setStatus(`Created ${result.business.name} with ${result.departments.length} departments and ${result.agents.length} agents.`);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Failed to create business.");
    }
  }

  return (
    <section className="card">
      <div className="section-title">Creation Studio</div>
      <h3 style={{ marginTop: 0 }}>+ Create</h3>
      <form onSubmit={submit} className="mini-list" style={{ marginBottom: 12 }}>
        <input value={name} onChange={(event) => setName(event.target.value)} placeholder="Business name" />
        <textarea value={purpose} onChange={(event) => setPurpose(event.target.value)} placeholder="Business purpose" />
        <button className="btn primary" type="submit">Create Business</button>
        {status && <div>{status}</div>}
      </form>
      <div className="mini-list">
        {createTypes.slice(0, 6).map((item) => <div key={item}>{item}</div>)}
      </div>
    </section>
  );
}
