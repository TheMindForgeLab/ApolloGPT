import ModelRouterPanel from "../models/ModelRouterPanel";
import MemoryViewer from "../memory/MemoryViewer";

export default function RightInspector() {
  return (
    <aside className="right-panel panel">
      <div className="section-title">Intelligence State</div>
      <div className="inspector-section">
        <h3>Context Packet</h3>
        <div className="mini-list">
          <div>Task: Create ApolloGPT UI</div>
          <div>Role: Manager Agent</div>
          <div>Scope: Project + Department</div>
          <div>Output: Implementation plan</div>
        </div>
      </div>
      <MemoryViewer />
      <div className="inspector-section">
        <h3>Active Agents</h3>
        <div className="mini-list">
          <div><span className="status-dot" /> Manager Agent: running</div>
          <div>Research Agent: idle</div>
          <div>Writer Agent: waiting</div>
          <div>Automation Agent: idle</div>
        </div>
      </div>
      <ModelRouterPanel />
      <div className="inspector-section">
        <h3>Next Actions</h3>
        <div className="mini-list">
          <div>Create business wizard</div>
          <div>Wire workflow canvas to backend</div>
          <div>Add live memory retrieval traces</div>
        </div>
      </div>
    </aside>
  );
}

