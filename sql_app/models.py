from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Member(Base):
    __tablename__ = "Member" # table name in the database

    Member_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, unique=True, index=True)
    Address = Column(String)
    Remark = Column(String, default=True)
    Phone=Column(String)

    # items = relationship("Item", back_populates="owner")
class product(Base):
    __tablename__ = "product" # table name in the database

    prodcut_ID = Column(Integer, primary_key=True, index=True)
    product_Name = Column(String, unique=True, index=True)
    product_Weight = Column(String)
    product_Price = Column(String, default=True)
