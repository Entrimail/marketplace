from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Category
from sqlalchemy.engine import Result
from sqlalchemy import select
from .schemas import CategoryCreateSchema, CategoryUpdateSchema


async def get_categories(session: AsyncSession) -> list[Category]:
    stmt = select(Category).order_by(Category.id)
    res: Result = await session.execute(stmt)
    categories = res.scalars()
    return list(categories)


async def get_category(session: AsyncSession, category_id: int) -> Category | None:
    return await session.get(Category, category_id)


async def create_category(session: AsyncSession, category_in: CategoryCreateSchema):
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()
    # await session.refresh(product)
    return category


async def update_category(
    session: AsyncSession,
    category: Category,
    category_update: CategoryUpdateSchema,
) -> Category:
    for name, value in category_update.model_dump(exclude_unset=False).items():
        setattr(category, name, value)
    await session.commit()
    return category


async def delete_category(session: AsyncSession, category: Category) -> None:
    await session.delete(category)
    await session.commit()
