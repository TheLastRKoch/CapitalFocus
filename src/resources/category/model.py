from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base, engine


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    # Relationships
    subcategory = relationship("Subcategory", back_populates="category")


Base.metadata.create_all(engine,  checkfirst=True)
