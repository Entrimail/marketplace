from pydantic import BaseModel


class CategoryBaseSchema(BaseModel):
    id: int
    name: str


class CategoryCreateSchema(BaseModel):
    name: str


class CategoryUpdateSchema(BaseModel):
    name: str | None = None
