from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime

from dummy_server.db.base import Base


class Message(Base):
    __tablename__ = 'message'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    count: Mapped[int] = mapped_column(default=1, unique=True)

    class Config:
        orm_mode = True

    def __repr__(self):
        return "<Message(id={}, user={})>".format(self.id, self.name)
