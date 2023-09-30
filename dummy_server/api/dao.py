from sqlalchemy import select, insert, func

from dummy_server.api.models import Message
from dummy_server.db.base import local_session


class MessageDataAccess:
    model = Message

    @classmethod
    async def post_message(cls, name, message, session):
        count = await cls._get_count(session, name)
        new_message = await session.execute(
            insert(cls.model).values(name=name, text=message, count=count + 1)
        )
        messages = await cls.get_last_messages(session, new_message.inserted_primary_key[0])
        return messages

    @classmethod
    async def _get_count(cls, session, name):
        count = await session.execute(
            select(func.count()).select_from(cls.model).where(cls.model.name == name)
        )
        return count.scalars().all()[0]

    @classmethod
    async def get_last_messages(cls, session, object_id):
        messages = await session.execute(
            select(cls.model).where(cls.model.id <= object_id).order_by(cls.model.id.desc()).limit(10)
        )
        return messages.scalars().all()
