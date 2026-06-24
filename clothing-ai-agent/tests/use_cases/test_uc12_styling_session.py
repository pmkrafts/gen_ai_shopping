from agent.styling_session_store import (
    create_session,
    get_session,
    update_session,
    clear_session,
)


def test_uc12_styling_session():
    clear_session()

    session = create_session(goal="beach vacation", budget=4000)
    assert session.goal == "beach vacation"
    assert session.budget == 4000

    update_session(feedback=["prefer bright colors"], turn_count=1)
    session = get_session()
    assert "prefer bright colors" in session.feedback
    assert session.turn_count == 1

    update_session(turn_count=2)
    session = get_session()
    assert session.turn_count == 2

    clear_session()
    assert get_session() is None
