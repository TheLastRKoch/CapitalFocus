from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base, engine


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    date = Column(String)
    userID = Column(String)
    reference = Column(String)
    amount = Column(Integer)
    type = Column(String)
    annotation = Column(String)

    # Relationships
    # sections = relationship("Section", secondary="section_transaction", back_populates="transactions")
    # Category = relationship("Subcategory", back_populates="transaction")


Base.metadata.create_all(engine,  checkfirst=True)
