from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class SolveRequest(BaseModel):
    problem_text: str | None = None
    image_ref: str | None = None   # id of a previously-ingested vision capture
    domain_hint: str | None = None  # e.g. "calculus", "fluid_dynamics", "crypto"


class SolveResponse(BaseModel):
    plan: list[str]
    result: str
    steps: list[str]


@router.post("", response_model=SolveResponse)
async def solve(req: SolveRequest) -> SolveResponse:
    """
    Entry point for the Master Planner -> Execution -> Verifier -> Synthesis
    agent pipeline. Currently a stub — wire this up to call
    agent-orchestrator's /run endpoint once that service is implemented.
    """
    # TODO: POST to settings.agent_orchestrator_url + "/run"
    return SolveResponse(
        plan=["decompose problem", "execute sub-tasks", "verify", "synthesize"],
        result="not yet implemented",
        steps=[],
    )
