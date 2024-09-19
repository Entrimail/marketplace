from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Order, OrderItem
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from .schemas import OrderUpdateSchema, OrderCreateSchema
from fastapi import HTTPException
from products.crud import get_product


async def get_orders(session: AsyncSession) -> list[Order]:
    stmt = select(Order).options(
        selectinload(Order.items).selectinload(OrderItem.product)
    )
    res: Result = await session.execute(stmt)
    orders = res.scalars().all()
    return list(orders)


async def get_order(session: AsyncSession, order_id: int) -> Order | None:
    stmt = (
        select(Order)
        .options(selectinload(Order.items).selectinload(OrderItem.product))
        .filter(Order.id == order_id)
    )
    result: Result = await session.execute(stmt)
    order = result.scalars().first()
    return order


async def create_order(session: AsyncSession, order_in: OrderCreateSchema):
    items = []
    for product_id, quantity in zip(order_in.items, order_in.quantities):
        product = await get_product(session=session, product_id=product_id)
        if not product or product.quantity < quantity:
            raise HTTPException(status_code=400, detail="The product is out of stock")

        product.quantity -= quantity
        items.append(OrderItem(product_id=product_id, quantity=quantity))
    order = Order(items=items)
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def update_order(
    session: AsyncSession,
    order: Order,
    status: OrderUpdateSchema,
) -> Order:
    if order:
        order.status = status.status
        await session.commit()
        return order
    else:
        raise HTTPException(status_code=404, detail="Order not found")
