from typing import Annotated
from fastapi import Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from . import crud
from core.models import db_helper, Order


async def order_by_id(
    order_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Order:
    order = await crud.get_order(session=session, order_id=order_id)
    if order:
        return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Order {order_id} is not found",
    )
