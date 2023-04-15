from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models

def get_user(db: Session, user_id: str):
    return db.query(models.Member).filter(models.Member.Name == user_id).first()
def save_change(db:Session,name:str,address:str,phone:str,remark:str,user_id:str):
    user=db.query(models.Member).filter(models.Member.Name == user_id).first()
    user.Name=name
    user.Address=address
    user.Phone=phone
    user.Remark=remark
    db.commit()
def add_data(db:Session,name:str,address:str,phone:str,remark:str,user_id:str):
    new_member=models.Member(Member_ID=user_id,Name=name,Address=address,Phone=phone,Remark=remark)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
def get_all_products(db:Session):
    return db.query(models.product).all()
# ,len(models.product.__table__.columns)
# [product.__dict__ for product in products]