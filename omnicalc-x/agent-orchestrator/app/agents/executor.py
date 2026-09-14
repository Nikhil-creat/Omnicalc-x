from app.state.reasoning_state import ReasoningState


async def execute(state: ReasoningState) -> ReasoningState:
    """
    Runs each planned sub-task inside a resource-limited sandbox
    (no network egress, CPU/memory quotas). Wire this to a restricted
    Python/SymPy/SciPy runtime or a WASM sandbox — never eval() directly
    in this process.
    """
    results = []
    for task in state.get("plan", []):
        # TODO: dispatch `task` to the sandboxed runner
        results.append(f"[unexecuted] {task}")
    state["execution_results"] = results
    return state
