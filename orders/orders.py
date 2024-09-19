from fastapi import APIRouter, Depends, HTTPException, status
from . import crud
from .schemas import (
    OrderCreateSchema,
    OrderUpdateSchema,
    OrderDetailResponse,
    OrderResponse,
)
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import order_by_id

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=list[OrderDetailResponse])
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_orders(session=session)


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_in: OrderCreateSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_order(session=session, order_in=order_in)


@router.get("/{order_id}/", response_model=OrderDetailResponse)
async def get_order(order=Depends(order_by_id)):
    return order


@router.put("/{order_id}/status")
async def update_order_status(
    status: OrderUpdateSchema,
    order=Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_order(session=session, order=order, status=status)
