export default function LeftPanel() {
  return (
    <aside className="left-panel panel">
      <div className="toolbar">
        <button className="btn primary">+ New</button>
        <button className="btn">Search</button>
      </div>

      <div className="section-title">Command</div>
      <nav>
        <div className="nav-item active">Chat</div>
        <div className="nav-item">Library</div>
        <div className="nav-item">Inbox</div>
      </nav>

      <div className="section-title">Businesses / Workspaces</div>
      <div className="tree-row active">Sterling Epoch</div>
      <div className="tree-row child">Research Department</div>
      <div className="tree-row child">Content Department</div>
      <div className="tree-row child">Automation Department</div>
      <div className="tree-row child">AI Operating System Project</div>

      <div className="section-title">System</div>
      <nav>
        {["Businesses", "Departments", "Projects", "Agents", "Workflows", "Tasks", "Memory", "Files", "Models", "LoRAs", "Personas", "Automations", "Nodes", "Settings"].map((item) => (
          <div className="nav-item" key={item}>{item}</div>
        ))}
      </nav>
    </aside>
  );
}
