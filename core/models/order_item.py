from .base import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.sql import func
from typing import TYPE_CHECKING
import datetime

if TYPE_CHECKING:
    from .order import Order
    from .product import Product


class OrderItem(Base):
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("product.id", ondelete="CASCADE"), nullable=False
    )
    quantity: Mapped[int] = mapped_column(nullable=False)
    order: Mapped["Order"] = relationship("Order", back_populates="items")
    product: Mapped["Product"] = relationship("Product")
