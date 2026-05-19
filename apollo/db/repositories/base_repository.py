from __future__ import annotations

import json
from typing import Any, Dict, Iterable, Optional

from apollo.db.database import get_connection, init_db
from apollo.schemas import new_id, utc_now


class BaseRepository:
    table = ""
    id_prefix = "row"
    json_fields: tuple[str, ...] = ()
    allowed_fields: tuple[str, ...] = ()

    def __init__(self):
        init_db()

    def _encode(self, data: Dict[str, Any]) -> Dict[str, Any]:
        encoded = dict(data)
        for field in self.json_fields:
            if field in encoded:
                encoded[f"{field}_json"] = json.dumps(encoded.pop(field), ensure_ascii=False)
        return encoded

    def _decode_row(self, row) -> Dict[str, Any]:
        data = dict(row)
        for key in list(data.keys()):
            if key.endswith("_json"):
                public_key = key[:-5]
                try:
                    data[public_key] = json.loads(data.pop(key) or "null")
                except json.JSONDecodeError:
                    data[public_key] = data.pop(key)
        return data

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        now = utc_now()
        row = {"id": data.get("id") or new_id(self.id_prefix), "created_at": now, "updated_at": now}
        for field in self.allowed_fields:
            if field in data:
                row[field] = data[field]
        row = self._encode(row)
        columns = ", ".join(row.keys())
        placeholders = ", ".join(f":{key}" for key in row.keys())
        with get_connection() as connection:
            connection.execute(f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders})", row)
        return self.get(row["id"])

    def list(self, filters: Optional[Dict[str, Any]] = None) -> list[Dict[str, Any]]:
        filters = {key: value for key, value in (filters or {}).items() if value not in {None, ""}}
        where = ""
        params: Dict[str, Any] = {}
        if filters:
            clauses = []
            for key, value in filters.items():
                if key not in self.allowed_fields and key != "id":
                    continue
                clauses.append(f"{key} = :{key}")
                params[key] = value
            if clauses:
                where = " WHERE " + " AND ".join(clauses)
        with get_connection() as connection:
            rows = connection.execute(f"SELECT * FROM {self.table}{where} ORDER BY created_at DESC", params).fetchall()
        return [self._decode_row(row) for row in rows]

    def get(self, row_id: str) -> Dict[str, Any] | None:
        with get_connection() as connection:
            row = connection.execute(f"SELECT * FROM {self.table} WHERE id = ?", (row_id,)).fetchone()
        return self._decode_row(row) if row else None

    def update(self, row_id: str, data: Dict[str, Any]) -> Dict[str, Any] | None:
        allowed = {key: value for key, value in data.items() if key in self.allowed_fields}
        if not allowed:
            return self.get(row_id)
        allowed["updated_at"] = utc_now()
        encoded = self._encode(allowed)
        assignments = ", ".join(f"{key} = :{key}" for key in encoded.keys())
        encoded["id"] = row_id
        with get_connection() as connection:
            connection.execute(f"UPDATE {self.table} SET {assignments} WHERE id = :id", encoded)
        return self.get(row_id)

