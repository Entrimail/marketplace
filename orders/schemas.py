from pydantic import BaseModel
from datetime import datetime


class OrderItemBaseSchema(BaseModel):
    product_id: int
    quantity: int


class OrderUpdateSchema(BaseModel):
    status: str


class ProductInOrderResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int

    class Config:
        from_attributes = True


class OrderCreateSchema(BaseModel):
    items: list[int]
    quantities: list[int]


class OrderResponse(BaseModel):
    id: int
    created_at: datetime
    status: str

    class Config:
        from_attributes = True


class OrderItemResponse(BaseModel):
    product: ProductInOrderResponse
    quantity: int

    class Config:
        from_attributes = True


class OrderDetailResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    items: list[OrderItemResponse]

    class Config:
        from_attributes = True
