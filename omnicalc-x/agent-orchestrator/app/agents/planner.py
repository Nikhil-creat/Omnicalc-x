from app.state.reasoning_state import ReasoningState


async def plan(state: ReasoningState) -> ReasoningState:
    """
    Decomposes the incoming problem into an ordered list of sub-tasks
    (a DAG in the full design; a flat ordered list is enough to start).
    """
    # TODO: call an LLM with a decomposition prompt, parse into sub-tasks
    state["plan"] = [f"analyze: {state['problem_text']}"]
    return state
