from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from sqlalchemy.engine import Result
from sqlalchemy import select
from .schemas import (
    ProductCreateSchema,
    ProductUpdateSchema,
)


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    res: Result = await session.execute(stmt)
    products = res.scalars()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreateSchema):
    product = Product(
        name=product_in.name,
        description=product_in.description,
        price=product_in.price,
        quantity=product_in.quantity,
    )

    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdateSchema,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=False).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: Product) -> None:
    await session.delete(product)
    await session.commit()
