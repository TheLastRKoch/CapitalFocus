from sqlalchemy import Column, Integer, String
from database import Base, engine


class UnclassifiedTransaction(Base):
    __tablename__ = "unclassifiedTransaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String)
    userID = Column(String)
    reference = Column(String)
    description = Column(String)
    amount = Column(Integer)
    type = Column(String)


Base.metadata.create_all(engine, checkfirst=True)
