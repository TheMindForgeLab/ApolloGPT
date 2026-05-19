import ChatWindow from "../chat/ChatWindow";
import TaskBoard from "../tasks/TaskBoard";
import WorkflowCanvas from "../workflow/WorkflowCanvas";
import CreationStudio from "../creation/CreationStudio";

const tabs = ["Chat", "Project", "Workflow", "Document", "Media", "Team Room"];

export default function CenterWorkspace() {
  return (
    <section className="center-panel">
      <div className="topbar">
        <div>
          <div className="brand">Apollo<span>GPT</span></div>
          <div style={{ color: "var(--muted)" }}>AI operating system command center</div>
        </div>
        <div className="toolbar">
          <button className="btn">Standard</button>
          <button className="btn primary">Advanced</button>
        </div>
      </div>

      <div className="workspace-tabs">
        {tabs.map((tab, index) => (
          <button key={tab} className={`workspace-tab ${index === 0 ? "active" : ""}`}>{tab}</button>
        ))}
      </div>

      <div className="grid two" style={{ marginBottom: 12 }}>
        <CreationStudio />
        <TaskBoard />
      </div>

      <ChatWindow />

      <div style={{ marginTop: 12 }}>
        <WorkflowCanvas />
      </div>
    </section>
  );
}

