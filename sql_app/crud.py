from sqlalchemy.orm import Session
from sqlalchemy.sql import or_
from sqlalchemy import func,desc,delete
from . import models
from datetime import date
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
    # return db.query(models.Member).filter(models.Order.order_number == od_nb).first()
    return db.query(models.Order).filter(models.Order.M_ID == user_id)
def add_order(db:Session,phone:str,Pick_up:str,m_id:int,remark:str,product_:dict,date_:date):
    try:
        max_value=db.query(models.Order).order_by(desc('order_number')).filter(models.Order.M_ID==m_id).first().order_number
    except:
        max_value=0
    su=0
    for key,value in product_.items():
        su+=product_[key][1]
    for key,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key ).first().prodcut_ID
        new_od=models.Order(order_number=max_value+1,M_ID=m_id,p_ID=pid,pick_up=Pick_up,pick_up_tf='0',count=value[0],Remark=remark,pick_up_date=date_,money=su)
        db.add(new_od)
        db.commit()
        db.refresh(new_od)
def get_od_info(db: Session, od_nb: int):
    # return db.query(models.Member).filter(models.Order.order_number == od_nb).first()
    return db.query(models.Order).filter(models.Order.order_number == od_nb).first()
def search_od_(db:Session,phone:str,pick_up:str,date_:date,money1:int,money2:int):   
    return db.query(models.Order).filter(or_(models.Order.phone== phone,models.Order.pick_up==pick_up,models.Order.Date_==date_,models.Order.money.between(money1,money2)))
def delete_od(db:Session,od_nb:int):
    db.query(models.Order).filter(models.Order.order_number == od_nb).delete()
    db.commit()
def get_edit_od(db:Session,od_nb:int,od_name:str):
    Mid=db.query(models.Member).filter(models.Member.Name==od_name).first().ID
    return db.query(models.Order).filter(models.Order.order_number==od_nb,models.Order.M_ID==Mid)
def edit_order_(db:Session,phone:str,Pick_up:str,m_id:int,remark:str,product_:dict,date_:date,key:int,M_name:str):
    Mid=db.query(models.Member).filter(models.Member.Name==M_name).first().ID
    db.query(models.Order).filter(models.Order.order_number==key,models.Order.M_ID==Mid).delete()
    db.commit()   
    try:
        max_value=db.query(models.Order).order_by(desc('order_number')).filter(models.Order.M_ID==m_id).first().order_number
    except:
        max_value=0
    su=0
    for key,value in product_.items():
        su+=product_[key][1]
    for key,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key ).first().prodcut_ID
        new_od=models.Order(phone=phone,order_number=max_value+1,M_ID=m_id,p_ID=pid,pick_up=Pick_up,pick_up_tf='0',count=value[0],Remark=remark,pick_up_date=date_,money=su)
        db.add(new_od)
        db.commit()
        db.refresh(new_od)
def delete_product(db:Session,p_id:int):
    db.query(models.product).filter(models.product.prodcut_ID == p_id).delete()
    db.commit()
def add_pd(db:Session,p_name:str,p_weight:str,p_price:int):
    new_pd=models.product(product_Name=p_name,product_Weight=p_weight,product_Price=p_price)
    db.add(new_pd)
    db.commit()
    db.refresh(new_pd)
def search_pd(db:Session,pd_name:str):
    if pd_name!="":
        return db.query(models.product).filter(models.product.product_Name==pd_name)
    return get_all_products(db=db)
def add_gift_box(db:Session,pd:dict,name:str,weight:str,price:int):
    content_=''
    i=1
    for key,value in pd.items():
        if i==1:
            content_+=f'{key}'
            i+=1
        else:content_+=f',{key}'
    new_pd=models.product(product_Name=name,product_Weight=weight,product_Price=price,content=content_)
    db.add(new_pd)
    db.commit()
    db.refresh(new_pd)
def get_balance(db:Session,od_nb:int,m_id:int):
    od=db.query(models.Order).filter(models.Order.M_ID==m_id,models.Order.order_number==od_nb).first()
    return od.money-od.collect_money
def update_balance(db:Session,od_nb:int,m_id:int,cm:int):
    od=db.query(models.Order).filter(models.Order.M_ID==m_id,models.Order.order_number==od_nb)
    for i in od:
        i.collect_money+=int(cm)
    db.commit()
    # return db.query(models.Order).filter(models.Order.money.between(money1,money2))
# ,len(models.product.__table__.columns)
# [product.__dict__ for product in products]