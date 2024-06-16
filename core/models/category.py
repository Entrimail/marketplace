from .base import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .product import Product


class Category(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    products: Mapped[list["Product"]] = relationship(
        "Product", cascade="all, delete-orphan"
    )
