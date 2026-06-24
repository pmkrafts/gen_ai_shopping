from agent.tool_wrapper import safe_tool_call


@safe_tool_call
def sample_tool(value: int):
    if value < 0:
        raise ValueError("value must be positive")
    return {"value": value}


def test_safe_tool_call_success():
    result = sample_tool(5)
    assert result["success"] is True
    assert result["data"] == {"value": 5}
    assert result["error"] is None


def test_safe_tool_call_failure():
    result = sample_tool(-1)
    assert result["success"] is False
    assert "positive" in result["error"]
