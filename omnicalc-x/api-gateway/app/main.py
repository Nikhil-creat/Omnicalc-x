"""
OmniCalc-X API Gateway
FastAPI async gateway: REST + WebSocket entrypoint, fronts the
vision-service, vector-db, and agent-orchestrator microservices.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.routers import solve, ingest, roadmap
from app.core.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: warm connections to vector-db / vision-service / agents here.
    yield
    # Shutdown: close connection pools here.


settings = get_settings()

app = FastAPI(
    title="OmniCalc-X API Gateway",
    version="0.1.0",
    description="Designed and developed by Nikhil Chary Sriramoju "
    "(github.com/Nikhil-creat | linkedin.com/in/nikhil-chary-sriramoju-95041b38a | "
    "nikhilsriramoju66@gmail.com)",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(solve.router, prefix="/api/solve", tags=["solve"])
app.include_router(ingest.router, prefix="/api/ingest", tags=["ingest"])
app.include_router(roadmap.router, prefix="/api/roadmap", tags=["roadmap"])


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.websocket("/ws/session")
async def session_socket(websocket: WebSocket):
    """
    Streams incremental agent reasoning steps back to the client as the
    Master Planner / Execution / Verifier / Synthesis agents complete.
    """
    await websocket.accept()
    try:
        while True:
            payload = await websocket.receive_json()
            # TODO: forward payload to agent-orchestrator, stream results back
            await websocket.send_json({"type": "ack", "received": payload})
    except WebSocketDisconnect:
        pass
