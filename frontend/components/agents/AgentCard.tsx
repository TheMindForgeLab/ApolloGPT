import AgentIntelligenceWizard from "./AgentIntelligenceWizard";

export default function AgentCard() {
  return (
    <div className="grid">
      <AgentIntelligenceWizard />
      <div className="card">
        <div className="section-title">Agent System</div>
        <h3 style={{ marginTop: 0 }}>Composable agents</h3>
        <div className="mini-list">
          <div>Base agent role</div>
          <div>Persona profile</div>
          <div>Skill mix</div>
          <div>LoRA / adapter stack</div>
          <div>Memory/RAG policy</div>
          <div>Model preference and fallback</div>
        </div>
      </div>
    </div>
  );
}
