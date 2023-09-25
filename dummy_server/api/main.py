from fastapi import FastAPI

from dummy_server.api.dao import MessageDataAccess
from dummy_server.api.schemas import MessageInput, MessageOut

app = FastAPI()


@app.post('/')
async def messages(message: MessageInput) -> list[MessageOut]:
    response = await MessageDataAccess.post_message(message.name, message.text)
    return response
