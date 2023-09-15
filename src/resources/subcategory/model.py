from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base, engine


class Subcategory(Base):
    __tablename__ = "subcategory"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    # Relationships
    # category = relationship("Category", back_populates="subcategory")
    # transactions = relationship("Transaction", back_populates="subcategory")


Base.metadata.create_all(engine,  checkfirst=True)
