from datetime import datetime

from pydantic import BaseModel, ConfigDict


class MessageInput(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    name: str
    text: str


class MessageOut(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    text: str
    date: datetime
    count: int
