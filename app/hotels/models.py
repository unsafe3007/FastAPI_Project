from app.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import JSON


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column()
    location: Mapped[str | None] = mapped_column()
    services: Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int | None] = mapped_column()
    image_id: Mapped[int] = mapped_column()
