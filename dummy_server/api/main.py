from aioredis import from_url
from fastapi import FastAPI

from dummy_server.api.dao import MessageDataAccess
from dummy_server.api.schemas import MessageInput, MessageOut
from dummy_server.config import settings

app = FastAPI()


# @app.on_event('startup')
# async def startup_event():
#     app.state.redis = from_url(settings.REDIS_URL)
#

@app.post('/')
async def messages(message: MessageInput) -> list[MessageOut]:
    # async with app.state.redis.lock('mutex'):
    response = await MessageDataAccess.post_message(message.name, message.text)
    return response
