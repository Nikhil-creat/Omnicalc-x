"""
OmniCalc-X Agent Orchestrator
Runs the Planner -> Execution -> Verifier -> Synthesis agent loop over a
LangGraph-style state machine.
"""
from fastapi import FastAPI
from pydantic import BaseModel

from app.graphs.reasoning_graph import build_reasoning_graph

app = FastAPI(title="OmniCalc-X Agent Orchestrator", version="0.1.0")
graph = build_reasoning_graph()


class RunRequest(BaseModel):
    problem_text: str
    latex: str | None = None
    domain_hint: str | None = None


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/run")
async def run(req: RunRequest):
    """Executes the full multi-agent DAG for a single problem."""
    result = await graph.arun(req.model_dump())
    return result
