from fastapi import APIRouter, Depends, HTTPException, status
from . import crud
from .schemas import CategoryBaseSchema, CategoryCreateSchema, CategoryUpdateSchema
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import category_by_id

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryBaseSchema])
async def get_categories(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_categories(session=session)


@router.post(
    "/", response_model=CategoryBaseSchema, status_code=status.HTTP_201_CREATED
)
async def create_category(
    category_in: CategoryCreateSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_category(session=session, category_in=category_in)


@router.get("/{category_id}/", response_model=CategoryBaseSchema)
async def get_category(category=Depends(category_by_id)):
    return category


@router.put("/{category_id}/")
async def update_category(
    category_update: CategoryUpdateSchema,
    category=Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_category(
        session=session, category=category, category_update=category_update
    )


@router.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category: CategoryBaseSchema = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_category(session=session, category=category)
