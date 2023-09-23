from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DB_HOST = '127.0.0.1'
DB_PORT = '5432'
DB_USER = 'mathgeni'
DB_PASS = '4242'
DB_NAME = 'learning'

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)

local_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
