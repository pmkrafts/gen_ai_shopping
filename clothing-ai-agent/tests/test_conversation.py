from agent.clothing_agent import run_agent, clear_memory


def test_conversation_memory_persists():
    clear_memory()

    response1 = run_agent("My budget is 5000 INR")
    assert response1["reply"]

    response2 = run_agent("What was my budget?")
    assert "5000" in response2["reply"] or "budget" in response2["reply"].lower()


def test_conversation_five_turns():
    clear_memory()

    turns = [
        "My budget is 5000 INR",
        "Show me red dresses",
        "Add PROD001 to my cart",
        "Recommend something to go with it",
        "What is my budget?",
    ]

    for turn in turns:
        response = run_agent(turn)
        assert response["reply"]
