from pydantic import BaseModel


class ProductBaseSchema(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class ProductCreateSchema(ProductBaseSchema):
    pass


class ProductResponse(ProductBaseSchema):
    id: int


class ProductUpdateSchema(ProductCreateSchema):
    pass


class ProductUpdatePartialSchema(ProductCreateSchema):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    category_id: int | None = None


class ProductUpdateScheme(ProductBaseSchema):
    pass
