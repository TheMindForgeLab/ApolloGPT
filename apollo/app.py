from __future__ import annotations

from apollo.bootstrap import build_orchestrator
from apollo.schemas import UserTask

try:
    from fastapi import FastAPI
    from apollo.api.agent_routes import router as agent_router
    from apollo.api.memory_routes import router as memory_router
    from apollo.api.workflow_routes import router as workflow_router
    from apollo.ui_api.business_routes import router as ui_business_router
    from apollo.ui_api.agent_routes import router as ui_agent_router
    from apollo.ui_api.dashboard_routes import router as ui_dashboard_router
    from apollo.ui_api.department_routes import router as ui_department_router
    from apollo.ui_api.log_routes import router as ui_log_router
    from apollo.ui_api.media_routes import router as ui_media_router
    from apollo.ui_api.model_routes import router as ui_model_router
    from apollo.ui_api.node_routes import router as ui_node_router
    from apollo.ui_api.project_routes import router as ui_project_router
    from apollo.ui_api.task_routes import router as ui_task_router
    from apollo.ui_api.voice_routes import router as ui_voice_router
except ImportError:  # pragma: no cover
    FastAPI = None


if FastAPI:
    app = FastAPI(title="ApolloGPT Backend", version="0.1.0")
    orchestrator = build_orchestrator()
    app.include_router(agent_router)
    app.include_router(memory_router)
    app.include_router(workflow_router)
    app.include_router(ui_business_router)
    app.include_router(ui_agent_router)
    app.include_router(ui_dashboard_router)
    app.include_router(ui_department_router)
    app.include_router(ui_log_router)
    app.include_router(ui_media_router)
    app.include_router(ui_model_router)
    app.include_router(ui_node_router)
    app.include_router(ui_project_router)
    app.include_router(ui_task_router)
    app.include_router(ui_voice_router)

    @app.get("/health")
    def health():
        return {"status": "ok", "system": "ApolloGPT"}

    @app.post("/chat")
    def chat(payload: dict):
        task = UserTask(
            input_text=payload.get("message", ""),
            project=payload.get("project", "ApolloGPT"),
            goal=payload.get("goal"),
            priority=payload.get("priority", "normal"),
            metadata=payload.get("metadata", {}),
        )
        validation = orchestrator.run_task(task)
        return {
            "response": validation.output,
            "success": validation.success,
            "score": validation.score,
            "issues": validation.issues,
            "agent_id": validation.raw_result.agent_id,
            "model_id": validation.raw_result.model_id,
            "task_id": task.id,
        }
else:
    app = None
