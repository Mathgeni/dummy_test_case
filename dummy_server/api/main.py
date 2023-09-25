from asyncio import Lock

from fastapi import FastAPI

from dummy_server.api.dao import MessageDataAccess
from dummy_server.api.schemas import MessageInput, MessageOut

app = FastAPI()

lock = Lock()


@app.post('/')
async def messages(message: MessageInput) -> list[MessageOut]:
    async with lock:
        response = await MessageDataAccess.post_message(message.name, message.text)
        return response
