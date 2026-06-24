from pydantic import BaseModel


class ToolCallResult(BaseModel):
    success: bool
    data: dict | list | str | None = None
    error: str | None = None
