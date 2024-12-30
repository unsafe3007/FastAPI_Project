from app.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column()
    hashed_password: Mapped[str] = mapped_column()
