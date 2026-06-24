from agent.guardrails import apply_guardrails, has_profanity, price_sanity_check


def test_apply_guardrails_allows_shopping_query():
    allowed, message = apply_guardrails("Show me red dresses")
    assert allowed is True
    assert message == ""


def test_apply_guardrails_rejects_off_topic():
    allowed, message = apply_guardrails("Who won the election?")
    assert allowed is False
    assert "clothing" in message.lower() or "fashion" in message.lower()


def test_apply_guardrails_rejects_empty():
    allowed, message = apply_guardrails("")
    assert allowed is False


def test_has_profanity():
    assert has_profanity("This is badword1!") is True
    assert has_profanity("Nice shirt") is False


def test_price_sanity_check():
    assert price_sanity_check(1500) is True
    assert price_sanity_check(-10) is False
    assert price_sanity_check(2_000_000) is False
    assert price_sanity_check(None) is True
