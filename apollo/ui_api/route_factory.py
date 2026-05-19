from __future__ import annotations

from fastapi import APIRouter


def make_resource_router(name: str) -> APIRouter:
    router = APIRouter(prefix=f"/api/{name}", tags=[name])

    @router.get("")
    def list_resource():
        return {"resource": name, "items": [], "status": "scaffold"}

    @router.get("/status")
    def resource_status():
        return {"resource": name, "status": "ready_for_implementation"}

    return router
