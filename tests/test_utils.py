import pytest
from agent.utils import retry


def test_retry_succeeds_first_time():
    result = retry(lambda: "ok", max_retries=2)
    assert result == "ok"


def test_retry_succeeds_after_failures():
    calls = {"count": 0}

    def flaky():
        calls["count"] += 1
        if calls["count"] < 3:
            raise RuntimeError("fail")
        return "success"

    result = retry(flaky, max_retries=3)
    assert result == "success"
    assert calls["count"] == 3


def test_retry_raises_after_exhausting_retries():
    def always_fail():
        raise RuntimeError("always fails")

    with pytest.raises(RuntimeError, match="always fails"):
        retry(always_fail, max_retries=1)
