from datetime import datetime

from sqlalchemy import select, insert, func

from dummy_server.api.models import Message
from dummy_server.db.base import local_session


class MessageDataAccess:
    model = Message

    @classmethod
    async def post_message(cls, name, text):
        async with local_session() as session:
            count = await cls._get_count(name)
            query = insert(cls.model).values(name=name, text=text, count=int(count[0]) + 1 if count[0] else 1)
            await session.execute(query)
            await session.commit()
            return await cls.get_last_messages()

    @classmethod
    async def _get_count(cls, name):
        async with local_session() as session:
            query = select(func.count()).select_from(cls.model).where(cls.model.name == name)
            count = await session.execute(query)
            return count.scalars().all()

    @classmethod
    async def get_last_messages(cls):
        async with local_session() as session:
            query = select(cls.model).order_by(cls.model.id.desc()).limit(10)
            messages = await session.execute(query)
            return messages.scalars().all()
