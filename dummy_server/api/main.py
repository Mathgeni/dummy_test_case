from typing import Annotated

from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dummy_server.api.dao import MessageDataAccess
from dummy_server.api.schemas import MessageInput, MessageOut
from dummy_server.db.base import local_session

app = FastAPI()


async def get_session() -> AsyncSession:  # type: ignore[misc]
    async with local_session.begin() as session:
        yield session


DatabaseSession = Annotated[AsyncSession, Depends(get_session)]


@app.post('/')
async def messages(session: DatabaseSession, message: MessageInput) -> list[MessageOut]:
    response = await MessageDataAccess.post_message(message.name, message.text, session)
    return response
