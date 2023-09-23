from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from dummy_server.config import settings

engine = create_async_engine(settings.DATABASE_URL)

local_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
