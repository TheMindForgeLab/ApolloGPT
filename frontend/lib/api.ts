const API_BASE = process.env.NEXT_PUBLIC_APOLLO_API_URL || "http://localhost:8000";

async function request(path: string, options: RequestInit = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {})
    }
  });
  if (!response.ok) {
    throw new Error(`Apollo API error ${response.status}`);
  }
  return response.json();
}

export async function sendChat(message: string) {
  const response = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, project: "ApolloGPT" })
  });
  return response.json();
}

export function listBusinesses() {
  return request("/api/businesses");
}

export function createBusiness(payload: Record<string, unknown>) {
  return request("/api/businesses", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function listDepartments(businessId?: string) {
  const query = businessId ? `?business_id=${encodeURIComponent(businessId)}` : "";
  return request(`/api/departments${query}`);
}

export function listProjects(businessId?: string) {
  const query = businessId ? `?business_id=${encodeURIComponent(businessId)}` : "";
  return request(`/api/projects${query}`);
}

export function listAgents(businessId?: string) {
  const query = businessId ? `?business_id=${encodeURIComponent(businessId)}` : "";
  return request(`/api/agents${query}`);
}

export function listTasks(businessId?: string) {
  const query = businessId ? `?business_id=${encodeURIComponent(businessId)}` : "";
  return request(`/api/tasks${query}`);
}

export function getAgentIntelligenceInventory() {
  return request("/api/agent-intelligence");
}

export function createPersona(payload: Record<string, unknown>) {
  return request("/api/agent-intelligence/personas", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function createSkill(payload: Record<string, unknown>) {
  return request("/api/agent-intelligence/skills", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function createLoRAProfile(payload: Record<string, unknown>) {
  return request("/api/agent-intelligence/loras", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function createMemoryPolicy(payload: Record<string, unknown>) {
  return request("/api/agent-intelligence/memory-policies", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}

export function createCustomAgent(payload: Record<string, unknown>) {
  return request("/api/agent-intelligence/agents", {
    method: "POST",
    body: JSON.stringify(payload)
  });
}
