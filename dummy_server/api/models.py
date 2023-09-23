from sqlalchemy import Column, Integer, Text, String, Date

from dummy_server.db.base import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date)
    count = Column(Integer)

    def __repr__(self):
        return "<Message(id={}, user={})>".format(self.id, self.user)
