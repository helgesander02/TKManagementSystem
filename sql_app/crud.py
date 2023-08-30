from sqlalchemy.orm import Session
from sqlalchemy.sql import or_,and_
from sqlalchemy import func,desc,delete
from . import models
from datetime import date
import tkinter as tk
def get_user(db: Session, user_phone: str):
    return db.query(models.member).filter(models.member.Phone == user_phone).first()
def save_change(db:Session,name:str,address:str,phone:str,remark:str,user_id:str):
    user=db.query(models.member).filter(models.member.Phone == user_id).first()
    user.Name=name
    user.Address=address
    user.Phone=phone
    user.Remark=remark
    db.commit()
def add_data(db:Session,name:str,address:str,phone:str,remark:str):
    new_member=models.member(Name=name,Address=address,Phone=phone,Remark=remark)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
def get_all_products(db:Session):
    return db.query(models.product).all()
def get_od(db: Session, user_id: int):
    # return db.query(models.Member).filter(models.Order.order_number == od_nb).first()
    return db.query(models.Order).filter(models.Order.M_ID == user_id)
def add_order(db:Session,phone:str,Pick_up:str,m_id:int,remark:str,product_:dict,date_:date,path:str,discount:int):
    try:
        mid=db.query(models.member).filter(models.member.Phone==phone.strip()).first().ID
    except:
        tk.messagebox.showinfo(title='失敗', message="未輸入電話或電話輸入錯誤", )
    try:
        max_value=db.query(models.Order).order_by(desc('order_number')).filter(models.Order.M_ID==mid).first().order_number
    except:
        max_value=0
    su=0
    i=0
    for key,value in product_.items():
        su+=product_[key][1]
    for key,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key ).first().prodcut_ID
        if i==0:
            new_od=models.Order(order_number=max_value+1,M_ID=mid,p_ID=pid,pick_up=Pick_up,pick_up_tf='否',count=value[0],Remark=remark,pick_up_date=date_,money=value[1],path=path,discount=discount,total=su-int(discount))
            i+=1
        else:
            new_od=models.Order(order_number=max_value+1,M_ID=mid,p_ID=pid,pick_up=Pick_up,pick_up_tf='否',count=value[0],Remark=remark,pick_up_date=date_,money=value[1],path=path,total=su-int(discount))
        db.add(new_od)
        db.commit()
        db.refresh(new_od)
def get_od_info(db: Session, od_nb: int):
    return db.query(models.Order).filter(models.Order.od_id == od_nb).first()
def search_od_(db:Session,phone:str,pick_up:str,date_:date,money1:int,money2:int,path:str):
    # or_(models.Order.Date_==date_),
    if phone=='':
        return db.query(models.Order).filter(models.Order.path.like(f'%{path}%'),models.Order.pick_up.like(f'%{pick_up}%'),models.Order.total.between(money1,money2),or_(models.Order.Date_==date_)).order_by(models.Order.pick_up_date)
    else:
        mid=db.query(models.member).filter(models.member.Phone==phone.strip()).first().ID
        return db.query(models.Order).filter(models.Order.M_ID== mid,models.Order.path.like(f'%{path}%'),models.Order.pick_up.like(f'%{pick_up}%'),models.Order.total.between(money1,money2),or_(models.Order.Date_==date_)).order_by(models.Order.pick_up_date)
def delete_od(db:Session,od_nb:int,m_id:int):
    db.query(models.Order).filter(models.Order.order_number == od_nb,models.Order.M_ID==m_id).delete()
    db.commit()
def get_edit_od(db:Session,od_nb:int,od_name:str):
    Mid=db.query(models.member).filter(models.member.Phone==od_name).first().ID
    return db.query(models.Order).filter(models.Order.order_number==od_nb,models.Order.M_ID==Mid).order_by(models.Order.od_id)
def edit_order_(db:Session,phone:str,Pick_up:str,path:str,remark:str,product_:dict,date_:date,key:int,M_name:str,discount:int):
    Mid=db.query(models.member).filter(models.member.Phone==M_name).first().ID
    db.query(models.Order).filter(models.Order.order_number==key,models.Order.M_ID==Mid).delete()
    db.commit()   
    now_od=key
    su=0
    i=0
    print(product_)
    for key_,value in product_.items():
        su+=product_[key_][1]
    for key_,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key_ ).first().prodcut_ID
        if i==0:
            new_od=models.Order(order_number=now_od,M_ID=Mid,p_ID=pid,pick_up=Pick_up,pick_up_tf='0',count=value[0],Remark=remark,pick_up_date=date_,money=value[1],total=su-int(discount),path=path,discount=discount)
            i+=1
        else:
            new_od=models.Order(order_number=now_od,M_ID=Mid,p_ID=pid,pick_up=Pick_up,pick_up_tf='0',count=value[0],Remark=remark,pick_up_date=date_,money=value[1],total=su-int(discount),path=path)
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
        return db.query(models.product).filter(models.product.product_Name.like(f'%{pd_name}%'))
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
def update_balance(db:Session,selected,cm:int,m_way:str,remark:str,discount:int):
    for key,value in selected.items():
      od=models.receipt(o_id=key,m_id=value,money=cm,m_way=m_way,remark=remark,discount=discount)
      db.add(od)  
      db.commit()
      db.refresh(od)
def home_search_date(db:Session,date_:date):
    return db.query(models.Order).filter(models.Order.Date_==date_)
def Search_receipt(db:Session,o_id:int,m_id:str):
    return db.query(models.receipt).filter(models.receipt.o_id==o_id,models.receipt.m_id==m_id)
def add_receipt(db:Session,o_id:int,m_id:int,money:int,m_way:str,remark:str,discount:int):
    new_receipt=models.receipt(o_id=o_id,m_id=m_id,money=money,m_way=m_way,remark=remark,discount=discount)
    db.add(new_receipt)
    db.commit()
    db.refresh(new_receipt)
def sum_receipt_money(db:Session,o_id:int,m_id:int):
    return db.query(func.sum(models.receipt.money)).filter(models.receipt.o_id==o_id,models.receipt.m_id==m_id).scalar(),db.query(models.Order).filter(models.Order.order_number==o_id,models.Order.M_ID==m_id).first().total
def ac_get_od(db:Session,o_nb,m_id):
    return db.query(models.Order).filter(models.Order.order_number==o_nb,models.Order.M_ID==m_id)
def spilt_bill_pd(db:Session,o_nb:int,phone:str):
    mid=db.query(models.member).filter(models.member.Phone==phone).first().ID
    return db.query(models.Order).filter(models.Order.order_number==o_nb,models.Order.M_ID==mid)
def spilt_bill_add(db:Session,phone:str,path:str,Pick_up:str,m_id:int,remark:str,product_:dict,date_:date,key:int,M_name:str,discount:int):
    #刪除原本的產品 product_ {'產品':[數量,價錢]}
    mid=db.query(models.member).filter(models.member.Phone==M_name).first().ID
    for i in product_.keys():
        pid=db.query(models.product).filter(models.product.product_Name == i ).first().prodcut_ID
        od=db.query(models.Order).filter(models.Order.order_number == key,models.Order.M_ID==mid,models.Order.p_ID==pid).first()
        if (od.count-product_[i][0])==0:
            db.query(models.Order).filter(models.Order.order_number == key,models.Order.M_ID==mid,models.Order.p_ID==pid).delete()
            db.commit()
        else:
            od=db.query(models.Order).filter(models.Order.order_number == key,models.Order.M_ID==mid,models.Order.p_ID==pid).first()
            od.count-=product_[i][0]
            db.commit()
    try:
        mid=db.query(models.member).filter(models.member.Phone==M_name).first().ID
    except:
        tk.messagebox.showinfo(title='失敗', message="請輸入電話", )
    try:
        max_value=db.query(models.Order).order_by(desc('order_number')).filter(models.Order.M_ID==mid).first().order_number
    except:
        max_value=0
    su=0
    i=0
    for key,value in product_.items():
        su+=product_[key][1]
    for key,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key ).first().prodcut_ID
        if i==0:
            new_od=models.Order(order_number=max_value+1,M_ID=mid,p_ID=pid,path=path,pick_up=Pick_up,pick_up_tf='0',count=value[0],Remark=remark,pick_up_date=date_,money=value[1],total=su-int(discount),discount=discount)
            i+=1
        else:
            new_od=models.Order(order_number=max_value+1,M_ID=mid,p_ID=pid,path=path,pick_up=Pick_up,pick_up_tf='0',count=value[0],Remark=remark,pick_up_date=date_,money=value[1],total=su-int(discount))
        
        db.add(new_od)
        db.commit()
        db.refresh(new_od)
def date_search(db:Session,date1,date2):
    od_count=db.query(models.Order.order_number,models.Order.M_ID).filter(models.Order.Date_.between(date1,date2)).distinct().count()
    pd_count=db.query(func.sum(models.Order.count)).filter(models.Order.Date_.between(date1,date2)).first()[0]
    p_count=db.query(models.Order.M_ID).filter(models.Order.Date_.between(date1,date2)).distinct().count()
    sum_money=db.query(func.sum(models.Order.money)).filter(models.Order.Date_.between(date1,date2)).first()[0]
    sum_discount=db.query(func.sum(models.Order.discount)).filter(models.Order.Date_.between(date1,date2)).first()[0]
    pd_count=0 if pd_count==None else pd_count
    sum_money=0 if sum_money==None else sum_money
    sum_discount=0 if sum_discount==None else sum_discount
    sum_profit=sum_money-sum_discount
    on_site=db.query(func.sum(models.Order.count),func.sum(models.Order.money)).filter(models.Order.Date_.between(date1,date2),models.Order.pick_up=='現場')[0]
    home_delivery=db.query(func.sum(models.Order.count),func.sum(models.Order.money)).filter(models.Order.Date_.between(date1,date2),models.Order.pick_up=='宅配')[0]

    p_on_site=db.query(func.sum(models.Order.count),func.sum(models.Order.money)).filter(models.Order.Date_.between(date1,date2),models.Order.path=='現場')[0]
    p_internet=db.query(func.sum(models.Order.count),func.sum(models.Order.money)).filter(models.Order.Date_.between(date1,date2),models.Order.path=='網站')[0]
    return od_count,pd_count,p_count,sum_money,sum_discount,sum_profit,on_site,home_delivery,p_on_site,p_internet
def pd_Analysis(db:Session,date1,date2):
    pd_1=db.query(models.Order).filter(models.Order.Date_.between(date1,date2))
    x=db.query(models.Order.p_ID).filter(models.Order.Date_.between(date1,date2))
    z=[]
    for i in x:
        z.append(i[0])
    pd_2=db.query(models.product).filter(models.product.prodcut_ID.not_in(z))
    pd_3={}
    for i in pd_1:#[數量,價錢]
        if i.p_ID_.product_Name in pd_3:
            pd_3[i.p_ID_.product_Name][0]+=i.count
            pd_3[i.p_ID_.product_Name][1]+=i.money
        else:
            pd_3[i.p_ID_.product_Name]=[i.count,i.money]
    for i in pd_2:
        pd_3[i.product_Name]=[0,0]
    return pd_3
def test(db:Session,money1:int,money2:int):
    return db.query(models.Order.M_ID,models.Order.order_number).filter(models.Order.total.between(money1,money2),).distinct()
def ac_us(db:Session,uid:int):
    return db.query(models.member).filter(models.member.ID==uid).first()
def get_good(db:Session,pid:int):
    return db.query(models.product).filter(models.product.prodcut_ID==pid).first()
def edit_good(db:Session,pid:int,p_name:str,p_weight:str,p_price:int):
    pd=db.query(models.product).filter(models.product.prodcut_ID==pid).first()
    pd.product_Name=p_name
    pd.product_Weight=p_weight
    pd.product_Price=p_price
    db.commit()
def member_search(db:Session,search:str,page:int):
    a=(page-1)*20
    b=page*20
    return db.query(models.member).filter(models.member.Phone.like(f'%{search}%'))[a:b],db.query(models.member).filter(models.member.Phone.like(f'%{search}%')).count()
def del_member(db:Session,id_:str):
    db.query(models.member).filter(models.member.ID==id_).delete()
    db.commit()
def get_member_count(db:Session):
    return db.query(models.member.ID).count()//20+1