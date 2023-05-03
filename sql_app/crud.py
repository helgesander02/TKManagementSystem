from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models

def get_user(db: Session, user_phone: str):
    return db.query(models.Member).filter(models.Member.Phone == user_phone).first()
def save_change(db:Session,name:str,address:str,phone:str,remark:str,user_id:str):
    user=db.query(models.Member).filter(models.Member.Name == user_id).first()
    user.Name=name
    user.Address=address
    user.Phone=phone
    user.Remark=remark
    db.commit()
def add_data(db:Session,name:str,address:str,phone:str,remark:str,user_id:str):
    new_member=models.Member(ID=user_id,Name=name,Address=address,Phone=phone,Remark=remark)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
def get_all_products(db:Session):
    return db.query(models.product).all()
def get_od(db: Session, user_id: int):
    # return db.query(models.Member).filter(models.Member.ID == user_id).first()
    return db.query(models.Order).filter(models.Order.M_ID == user_id)
def add_order(db:Session,phone:str,Pick_up:str,m_id:int,remark:str,product_:dict):
    print(phone,Pick_up,m_id,remark,product_)
    max_value=db.query(models.Order).order_by('order_number').filter(models.Order.M_ID==m_id).first().order_number
    
    for key,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key ).first().prodcut_ID
        new_od=models.Order(order_number=max_value+1,M_ID=m_id,p_ID=pid,pick_up=Pick_up,pick_up_tf='0',count=value[0],Remark=remark)
        db.add(new_od)
        db.commit()
        db.refresh(new_od)

# ,len(models.product.__table__.columns)
# [product.__dict__ for product in products]