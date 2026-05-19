"use client";

import { useEffect, useState } from "react";
import { listTasks } from "../../lib/api";
import type { Task } from "../../lib/types";

export default function TaskBoard() {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    listTasks().then((data) => setTasks(data.items || [])).catch(() => undefined);
  }, []);

  const done = tasks.filter((task) => task.status === "done").length;
  const active = tasks.filter((task) => ["active", "running", "in_progress"].includes(task.status)).length;

  return (
    <section className="card">
      <div className="section-title">Project Tasks</div>
      <div className="grid three">
        <div><strong>{tasks.length}</strong><br />Total</div>
        <div><strong style={{ color: "var(--green)" }}>{done}</strong><br />Done</div>
        <div><strong style={{ color: "var(--blue)" }}>{active}</strong><br />Active</div>
      </div>
    </section>
  );
}
