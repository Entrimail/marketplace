from .base import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from typing import TYPE_CHECKING
import datetime

if TYPE_CHECKING:
    from .order_item import OrderItem


class Order(Base):
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    status: Mapped[str] = mapped_column(nullable=False, default="in proccess")

    items: Mapped[list["OrderItem"]] = relationship("OrderItem", back_populates="order")
