import re
from pydantic import BaseModel, Field, field_validator


class Product(BaseModel):
    id: str = Field(..., pattern=r"^PROD\d{3}$")
    title: str
    price: float = Field(..., gt=0)
    currency: str = "INR"
    sizes: list[str]
    colors: list[str]
    description: str
    tags: list[str]
    category: str
    gender: str
    image_url: str | None = None
    stock: int = Field(..., ge=0)

    @field_validator("id")
    @classmethod
    def id_must_match_pattern(cls, v: str) -> str:
        if not re.match(r"^PROD\d{3}$", v):
            raise ValueError("Product ID must match PROD###")
        return v
