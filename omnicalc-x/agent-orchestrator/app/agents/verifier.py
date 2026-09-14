from app.state.reasoning_state import ReasoningState


async def verify(state: ReasoningState) -> ReasoningState:
    """
    Cross-checks execution results against known constraints (units,
    boundary conditions, alternative solving methods) to catch
    hallucinated or numerically divergent results before synthesis.
    """
    # TODO: run sanity checks / alternate-method cross-validation
    state["verification_notes"] = ["not yet verified"]
    return state
