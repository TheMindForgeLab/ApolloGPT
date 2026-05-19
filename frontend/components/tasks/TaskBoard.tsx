export default function TaskBoard() {
  return (
    <section className="card">
      <div className="section-title">Project Tasks</div>
      <div className="grid three">
        <div><strong>128</strong><br />Total</div>
        <div><strong style={{ color: "var(--green)" }}>86</strong><br />Done</div>
        <div><strong style={{ color: "var(--blue)" }}>24</strong><br />Active</div>
      </div>
    </section>
  );
}

