from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table,DateTime
from sqlalchemy.orm import relationship,session,Mapped,mapped_column
from datetime import datetime
from .database import Base
# association_table=Table(
#     "association_table",
#     Base.metadata,
#     Column("M_id", Integer, ForeignKey("Member.ID")),
#     Column("p_id", Integer, ForeignKey("product.prodcut_ID")),
#     Column('od_ID', Integer, ForeignKey('order.od_ID'))
# )

class Order(Base):
    __tablename__ = "order"
    od_id=Column(Integer, primary_key=True)
    order_number=Column(Integer)
    M_ID=Column(ForeignKey("Member.ID"))
    p_ID=Column(ForeignKey("product.prodcut_ID"))
    M_ID_=relationship('Member', back_populates='orders')
    p_ID_=relationship('product', back_populates='orders')
    # p_ID_=relationship('product', secondary=association_table, back_populates='orders',overlaps='M_ID')
    Date_=Column(DateTime, default=datetime.now)
    pick_up=Column(String)
    pick_up_tf=Column(String)
    count=Column(Integer)
    Remark=Column(String)
    pick_up_date=Column(DateTime)
    money=Column(Integer)
    phone=Column(String)
    collect_money=Column(Integer,default=0)
class Member(Base):
    __tablename__ = "Member" # table name in the database

    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String, unique=True, index=True)
    Address = Column(String)
    Remark = Column(String, default=True)
    Phone=Column(String)
    orders = relationship('Order', back_populates='M_ID_')

    # items = relationship("Item", back_populates="owner")
class product(Base):
    __tablename__ = "product" # table name in the database

    prodcut_ID = Column(Integer, primary_key=True, index=True)
    product_Name = Column(String, unique=True, index=True)
    product_Weight = Column(String)
    product_Price = Column(String, default=True)
    orders = relationship('Order', back_populates='p_ID_')
    content=Column(String)
    # orders = relationship('Order', secondary=association_table, back_populates='p_ID_',overlaps="M_ID")
class receipt(Base):
    __tablename__ = "receipt"

    rc_id=Column(Integer, primary_key=True, index=True)
    o_id=Column(Integer)
    m_id=Column(ForeignKey("Member.ID"))
    date=Column(DateTime, default=datetime.now)
    money=Column(Integer)
    remark=Column(String)
    m_way=Column(String)
    discount=Column(Integer)