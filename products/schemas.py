from pydantic import BaseModel


class ProductBaseSchema(BaseModel):
    name: str
    description: str
    price: float
    category_id: int


class ProductCreateSchema(BaseModel):
    name: str
    description: str
    price: float
    category_id: int


class ProductUpdateSchema(ProductCreateSchema):
    pass


class ProductUpdatePartialSchema(ProductCreateSchema):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    category_id: int | None = None
