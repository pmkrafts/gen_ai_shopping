from agent.styling_session_store import (
    create_session,
    get_session,
    update_session,
    clear_session,
)


def test_create_and_get_session():
    clear_session()
    session = create_session(goal="beach vacation", budget=5000)
    assert session.goal == "beach vacation"
    assert session.budget == 5000
    assert get_session() is session


def test_update_session():
    clear_session()
    create_session(goal="wedding outfit")
    updated = update_session(budget=8000, turn_count=1)
    assert updated.budget == 8000
    assert updated.turn_count == 1


def test_clear_session():
    clear_session()
    create_session(goal="party outfit")
    clear_session()
    assert get_session() is None
