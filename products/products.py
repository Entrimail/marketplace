from fastapi import APIRouter, Depends, HTTPException, status
from . import crud
from .schemas import (
    ProductBaseSchema,
    ProductCreateSchema,
    ProductUpdatePartialSchema,
    ProductUpdateSchema,
)
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import product_by_id

router = APIRouter(prefix="/products", tags=["Products"])


@router.get(
    "/",
)
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreateSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/")
async def get_product(product=Depends(product_by_id)):
    return product


@router.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdateSchema,
    product=Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session, product=product, product_update=product_update, partial=False
    )


@router.patch("/{product_id}/")
async def update_product_partial(
    product_update: ProductUpdatePartialSchema,
    product=Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(
        session=session, product=product, product_update=product_update, partial=True
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: ProductBaseSchema = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)


@router.get("-by-id/{category_id}/")
async def get_products_by_category(
    category_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products_by_category(session=session, category_id=category_id)
