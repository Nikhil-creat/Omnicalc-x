from typing import TypedDict


class ReasoningState(TypedDict, total=False):
    problem_text: str
    latex: str | None
    domain_hint: str | None

    plan: list[str]              # sub-tasks from the Master Planner
    execution_results: list[str]  # raw outputs from the Execution Engine
    verification_notes: list[str]  # Critic agent's pass/fail + rationale
    final_answer: str
    explanation_steps: list[str]
