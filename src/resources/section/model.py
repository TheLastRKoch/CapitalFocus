from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine


class Section(Base):
    __tablename__ = "section"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    ExpenseEstimate = Column(String)

    # Relationships
    # budget = relationship("Budget", back_populates="section")
    # transactions = relationship("Transaction", secondary="section_transaction", back_populates="sections")


# class SectionTransaction(Base):
#     __tablename__ = "section_transaction"
#     section_id = Column(Integer, ForeignKey("transaction.id"), primary_key=True)
#     transaction_id = Column(Integer, ForeignKey("section.id"), primary_key=True)


Base.metadata.create_all(engine,  checkfirst=True)
