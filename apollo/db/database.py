from __future__ import annotations

import sqlite3
from pathlib import Path

from apollo.settings import settings


SCHEMA = """
CREATE TABLE IF NOT EXISTS businesses (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    business_type TEXT NOT NULL DEFAULT 'Custom',
    purpose TEXT NOT NULL DEFAULT '',
    goals_json TEXT NOT NULL DEFAULT '[]',
    brand_voice TEXT NOT NULL DEFAULT '',
    constraints_json TEXT NOT NULL DEFAULT '[]',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS departments (
    id TEXT PRIMARY KEY,
    business_id TEXT NOT NULL,
    name TEXT NOT NULL,
    purpose TEXT NOT NULL DEFAULT '',
    manager_agent_id TEXT,
    allowed_tools_json TEXT NOT NULL DEFAULT '[]',
    memory_scope TEXT NOT NULL DEFAULT 'department',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (business_id) REFERENCES businesses(id)
);

CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    business_id TEXT,
    department_id TEXT,
    name TEXT NOT NULL,
    goal TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'active',
    progress INTEGER NOT NULL DEFAULT 0,
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (business_id) REFERENCES businesses(id),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE IF NOT EXISTS agents (
    id TEXT PRIMARY KEY,
    business_id TEXT,
    department_id TEXT,
    name TEXT NOT NULL,
    agent_type TEXT NOT NULL DEFAULT 'specialist',
    role TEXT NOT NULL DEFAULT '',
    persona TEXT NOT NULL DEFAULT '',
    preferred_model TEXT NOT NULL DEFAULT '',
    fallback_model TEXT NOT NULL DEFAULT '',
    memory_access_json TEXT NOT NULL DEFAULT '[]',
    tool_access_json TEXT NOT NULL DEFAULT '[]',
    workflow_permissions_json TEXT NOT NULL DEFAULT '[]',
    lora_profile TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'idle',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (business_id) REFERENCES businesses(id),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE IF NOT EXISTS tasks (
    id TEXT PRIMARY KEY,
    business_id TEXT,
    department_id TEXT,
    project_id TEXT,
    agent_id TEXT,
    title TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'backlog',
    priority TEXT NOT NULL DEFAULT 'normal',
    progress INTEGER NOT NULL DEFAULT 0,
    output_ref TEXT NOT NULL DEFAULT '',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (business_id) REFERENCES businesses(id),
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (agent_id) REFERENCES agents(id)
);

CREATE TABLE IF NOT EXISTS automations (
    id TEXT PRIMARY KEY,
    business_id TEXT,
    department_id TEXT,
    project_id TEXT,
    name TEXT NOT NULL,
    trigger_json TEXT NOT NULL DEFAULT '{}',
    conditions_json TEXT NOT NULL DEFAULT '[]',
    workflow_name TEXT NOT NULL DEFAULT '',
    approval_required INTEGER NOT NULL DEFAULT 1,
    status TEXT NOT NULL DEFAULT 'draft',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (business_id) REFERENCES businesses(id),
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE IF NOT EXISTS personas (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    tone TEXT NOT NULL DEFAULT '',
    rules_json TEXT NOT NULL DEFAULT '[]',
    examples_json TEXT NOT NULL DEFAULT '[]',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS skills (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    skill_type TEXT NOT NULL DEFAULT 'general',
    instructions TEXT NOT NULL DEFAULT '',
    tools_json TEXT NOT NULL DEFAULT '[]',
    input_types_json TEXT NOT NULL DEFAULT '[]',
    output_types_json TEXT NOT NULL DEFAULT '[]',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lora_profiles (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    lora_type TEXT NOT NULL DEFAULT 'text',
    base_model TEXT NOT NULL DEFAULT '',
    trigger_phrase TEXT NOT NULL DEFAULT '',
    strength REAL NOT NULL DEFAULT 1.0,
    adapter_path TEXT NOT NULL DEFAULT '',
    allowed_models_json TEXT NOT NULL DEFAULT '[]',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS memory_policies (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    scopes_json TEXT NOT NULL DEFAULT '[]',
    retrieval_limit INTEGER NOT NULL DEFAULT 8,
    include_summaries INTEGER NOT NULL DEFAULT 1,
    include_graph INTEGER NOT NULL DEFAULT 1,
    include_files INTEGER NOT NULL DEFAULT 1,
    rules_json TEXT NOT NULL DEFAULT '[]',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS agent_intelligence_profiles (
    id TEXT PRIMARY KEY,
    agent_id TEXT NOT NULL,
    persona_id TEXT,
    memory_policy_id TEXT,
    skill_ids_json TEXT NOT NULL DEFAULT '[]',
    lora_profile_ids_json TEXT NOT NULL DEFAULT '[]',
    style_profile_json TEXT NOT NULL DEFAULT '{}',
    domain_packs_json TEXT NOT NULL DEFAULT '[]',
    system_instructions TEXT NOT NULL DEFAULT '',
    metadata_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (agent_id) REFERENCES agents(id),
    FOREIGN KEY (persona_id) REFERENCES personas(id),
    FOREIGN KEY (memory_policy_id) REFERENCES memory_policies(id)
);
"""


def get_connection(path: Path | None = None) -> sqlite3.Connection:
    db_path = path or settings.database_path
    db_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db(path: Path | None = None) -> None:
    with get_connection(path) as connection:
        connection.executescript(SCHEMA)
