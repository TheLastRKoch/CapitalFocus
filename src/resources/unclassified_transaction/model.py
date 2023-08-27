from sqlalchemy import Column, Integer, String
from database import Base, engine


class unclassifiedTransaction(Base):
    __tablename__ = "unclassifiedTransaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    reference = Column(String)
    amount = Column(Integer)
    type = Column(String)
    date = Column(String)
    userID = Column(String)


Base.metadata.create_all(engine,  checkfirst=True)
