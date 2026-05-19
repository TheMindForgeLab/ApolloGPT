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
