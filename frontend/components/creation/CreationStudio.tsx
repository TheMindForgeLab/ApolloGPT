const createTypes = ["Business", "Department", "Project", "Agent", "Persona", "Workflow", "Task", "Memory Pack", "LoRA Profile", "Automation"];

export default function CreationStudio() {
  return (
    <section className="card">
      <div className="section-title">Creation Studio</div>
      <h3 style={{ marginTop: 0 }}>+ Create</h3>
      <div className="mini-list">
        {createTypes.slice(0, 6).map((item) => <div key={item}>{item}</div>)}
      </div>
    </section>
  );
}

