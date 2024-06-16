from .base import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey
from .category import Category


class Product(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    category: Mapped["Category"] = relationship(back_populates="products")
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
