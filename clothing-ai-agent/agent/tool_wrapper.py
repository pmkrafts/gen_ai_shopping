from typing import Callable
from functools import wraps
from models.tool_result import ToolCallResult


def safe_tool_call(func: Callable) -> Callable:
    """Decorator that wraps a tool function and returns a ToolCallResult.

    On success: returns ToolCallResult(success=True, data=result)
    On failure: returns ToolCallResult(success=False, error=str(e))
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return ToolCallResult(success=True, data=result).model_dump()
        except Exception as e:
            return ToolCallResult(success=False, error=str(e)).model_dump()

    return wrapper
