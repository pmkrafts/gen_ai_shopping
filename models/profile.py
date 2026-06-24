from pydantic import BaseModel


class UserProfile(BaseModel):
    name: str | None = None
    age: int | None = None
    gender: str | None = None
    height: str | None = None
    weight: str | None = None
    size: str | None = None
    budget: float | None = None
    style: list[str] = []
    region: str | None = None
