"use client";

import { useEffect, useState } from "react";
import { listAgents, listBusinesses, listDepartments, listProjects, listTasks } from "../../lib/api";
import type { Agent, Business, Department, Project, Task } from "../../lib/types";

export default function BusinessDashboard() {
  const [businesses, setBusinesses] = useState<Business[]>([]);
  const [departments, setDepartments] = useState<Department[]>([]);
  const [projects, setProjects] = useState<Project[]>([]);
  const [agents, setAgents] = useState<Agent[]>([]);
  const [tasks, setTasks] = useState<Task[]>([]);
  const activeBusiness = businesses[0];

  useEffect(() => {
    async function load() {
      const businessData = await listBusinesses();
      setBusinesses(businessData.items || []);
      const first = businessData.items?.[0];
      if (first) {
        const [departmentData, projectData, agentData, taskData] = await Promise.all([
          listDepartments(first.id),
          listProjects(first.id),
          listAgents(first.id),
          listTasks(first.id)
        ]);
        setDepartments(departmentData.items || []);
        setProjects(projectData.items || []);
        setAgents(agentData.items || []);
        setTasks(taskData.items || []);
      }
    }
    load().catch(() => undefined);
  }, []);

  return (
    <div className="card">
      <div className="section-title">Business Dashboard</div>
      <h3 style={{ marginTop: 0 }}>{activeBusiness?.name || "No business created yet"}</h3>
      <p style={{ color: "var(--muted)" }}>{activeBusiness?.purpose || "Use Creation Studio to create the first business."}</p>
      <div className="grid three">
        <div><strong>{departments.length}</strong><br />Departments</div>
        <div><strong>{agents.length}</strong><br />Agents</div>
        <div><strong>{projects.length}</strong><br />Projects</div>
      </div>
      <div style={{ marginTop: 12 }}>
        <strong>Open Tasks</strong>
        <div className="mini-list">
          {tasks.slice(0, 5).map((task) => <div key={task.id}>{task.title} · {task.status}</div>)}
          {!tasks.length && <div>No tasks yet.</div>}
        </div>
      </div>
    </div>
  );
}
