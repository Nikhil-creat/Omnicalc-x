"""
Wires Planner -> Executor -> Verifier -> Synthesizer into a graph.

This stub runs the four stages sequentially. Swap in LangGraph's
StateGraph for real cyclic control flow (e.g. looping back to the
Executor when the Verifier rejects a result).
"""
from app.agents.executor import execute
from app.agents.planner import plan
from app.agents.synthesizer import synthesize
from app.agents.verifier import verify
from app.state.reasoning_state import ReasoningState


class ReasoningGraph:
    async def arun(self, initial_state: dict) -> ReasoningState:
        state: ReasoningState = initial_state  # type: ignore[assignment]
        state = await plan(state)
        state = await execute(state)
        state = await verify(state)
        state = await synthesize(state)
        return state


def build_reasoning_graph() -> ReasoningGraph:
    # TODO: replace with a real langgraph.graph.StateGraph once the
    # verify -> execute retry loop is needed.
    return ReasoningGraph()
