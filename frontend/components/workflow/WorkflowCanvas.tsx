const nodes = ["Trigger", "Memory", "Research Agent", "Writer Agent", "Approval", "Memory Write"];

export default function WorkflowCanvas() {
  return (
    <section className="card">
      <div className="section-title">Workflow Builder</div>
      <div className="workflow-canvas">
        <div>
          <strong>Node Palette</strong>
          {["Trigger", "Agent", "Department", "Memory", "Logic", "Tool"].map((item) => (
            <div className="node-card" key={item}>{item}</div>
          ))}
        </div>
        <div>
          <strong>Canvas</strong>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 10 }}>
            {nodes.map((node) => <div className="node-card" key={node}>{node}</div>)}
          </div>
        </div>
        <div>
          <strong>Run Console</strong>
          <div className="mini-list" style={{ marginTop: 10 }}>
            <div>Design View</div>
            <div>Test View</div>
            <div>Live Run</div>
            <div>Logs</div>
          </div>
        </div>
      </div>
    </section>
  );
}

