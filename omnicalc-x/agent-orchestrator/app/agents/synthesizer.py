from app.state.reasoning_state import ReasoningState


async def synthesize(state: ReasoningState) -> ReasoningState:
    """Turns verified results into a step-by-step, human-readable explanation."""
    # TODO: call an LLM to write the pedagogical breakdown
    state["final_answer"] = state.get("execution_results", ["(no result)"])[-1]
    state["explanation_steps"] = state.get("plan", [])
    return state
