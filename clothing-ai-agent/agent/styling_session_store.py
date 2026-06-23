from models.styling_session import StylingSession

_session: StylingSession | None = None


def get_session() -> StylingSession | None:
    return _session


def create_session(goal: str, budget: float | None = None) -> StylingSession:
    global _session
    _session = StylingSession(goal=goal, budget=budget)
    return _session


def update_session(**kwargs) -> StylingSession:
    global _session
    if _session is None:
        raise ValueError("No active styling session")
    data = _session.model_dump()
    data.update(kwargs)
    _session = StylingSession(**data)
    return _session


def clear_session() -> None:
    global _session
    _session = None
