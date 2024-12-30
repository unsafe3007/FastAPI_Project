# В этом файле находится всё что связано с подключением к БД
# ____________________________________________________________

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)  # Создаеём движек

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
