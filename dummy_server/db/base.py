from typing import Final

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from dummy_server.config import settings

POOL_RECYCLE: Final[int] = 60 * 5

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_recycle=POOL_RECYCLE,
    # isolation_level="SERIALIZABLE",
)

local_session = sessionmaker(  # type: ignore[call-overload]
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


class Base(DeclarativeBase):
    pass
