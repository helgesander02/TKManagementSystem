from sqlalchemy.orm import Session
from sqlalchemy.sql import or_,and_
from sqlalchemy import func,desc,delete,Connection,text
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
    max_value=0
    if db.query(models.order_new).order_by(desc('order_number')).filter(models.order_new.m_id==mid).first()!=None:
        max_value=db.query(models.order_new).order_by(desc('order_number')).filter(models.order_new.m_id==mid).first().order_number
    su=sum(i[1] for i in product_.values())
    new=models.order_new(order_number=max_value+1,m_id=mid,pick_up=Pick_up,pick_up_tf='否',remark=remark,pick_up_date=date_,path=path,discount=discount,total=su-int(discount))
    db.add(new)
    db.commit()
    db.refresh(new)
    id_=db.query(models.order_new).filter(models.order_new.order_number==max_value+1,models.order_new.m_id==mid).first().id
    for key,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key ).first().prodcut_ID
        new_od=models.order_list(p_id=pid,od_id=id_,count=value[0],money=value[1])
        db.add(new_od)
        db.commit()
        db.refresh(new_od)
def get_od_info(db: Session, od_nb: int):
    return db.query(models.order_new).filter(models.order_new.id == od_nb).first()
def search_od_(db:Session,phone:str,pick_up:str,date_:date,date_1:date,money1:int,money2:int,path:str,page:int):
    # or_(models.Order.Date_==date_),
    a=(page-1)*20
    b=page*20
    if phone=='':
        return db.query(models.order_new).filter(models.order_new.path.like(f'%{path}%'),models.order_new.pick_up.like(f'%{pick_up}%'),models.order_new.total.between(money1,money2),models.order_new.pick_up_date.between(date_,date_1)).order_by(models.order_new.pick_up_date)[a:b],db.query(models.order_new).filter(models.order_new.path.like(f'%{path}%'),models.order_new.pick_up.like(f'%{pick_up}%'),models.order_new.total.between(money1,money2),models.order_new.pick_up_date.between(date_,date_1)).order_by(models.order_new.pick_up_date).count()
    else:
        mid=db.query(models.member).filter(models.member.Phone==phone.strip()).first().ID
        return db.query(models.order_new).filter(models.order_new.M_ID== mid,models.order_new.path.like(f'%{path}%'),models.order_new.pick_up.like(f'%{pick_up}%'),models.order_new.total.between(money1,money2),models.order_new.pick_up_date.between(date_,date_1)).order_by(models.order_new.pick_up_date)[a:b],db.query(models.order_new).filter(models.order_new.path.like(f'%{path}%'),models.order_new.pick_up.like(f'%{pick_up}%'),models.order_new.total.between(money1,money2),models.order_new.pick_up_date.between(date_,date_1)).order_by(models.order_new.pick_up_date).count()
def delete_od(db:Session,id_:int):
    db.query(models.order_new).filter(models.order_new.id==id_).delete()
    db.commit()
def get_edit_od(db:Session,id_):
    # Mid=db.query(models.member).filter(models.member.Phone==od_name).first().ID
    return db.query(models.order_new).filter(models.order_new.id==id_).first()
def edit_order_(db:Session,phone:str,Pick_up:str,path:str,remark:str,product_:dict,date_:date,id:int,discount:int):
    su=sum(i[1] for i in product_.values())
    od_=db.query(models.order_new).filter(models.order_new.id==id).first()
    od_.pick_up=Pick_up
    od_.remark=remark
    od_.pick_up_date=date_
    od_.total=su-int(discount)
    od_.discount=discount
    od_.path=path
    db.commit()
    db.query(models.order_list).filter(models.order_list.od_id==id).delete()
    db.commit()

    for key_,value in product_.items():
        pid=db.query(models.product).filter(models.product.product_Name == key_ ).first().prodcut_ID
        new_od=models.order_list(p_id=pid,od_id=id,count=value[0],money=value[1])
        db.add(new_od)
        db.commit()
        db.refresh(new_od)
def delete_product(db:Session,p_id:int):
    db.query(models.product).filter(models.product.prodcut_ID == p_id).delete()
    db.commit()
def delete_all_pd(db:Session):
    # db.execute(text('DELETE FROM product'))
    # Connection.execute('DELETE FROM product')
    db.query(models.product).filter().delete()
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
def home_search_date(db:Session,date_:date,page:int):
    a=(page-1)*20
    b=page*20
    return db.query(models.order_new).filter(models.order_new.pick_up_date==date_).order_by(models.order_new.pick_up_date)[a:b],db.query(models.order_new).filter(models.order_new.pick_up_date==date_).order_by(models.order_new.pick_up_date).count()
def Search_receipt(db:Session,o_id:int,m_id:str):
    return db.query(models.receipt).filter(models.receipt.o_id==o_id,models.receipt.m_id==m_id)
def add_receipt(db:Session,o_id:int,m_id:int,money:int,m_way:str,remark:str,discount:int):
    new_receipt=models.receipt(o_id=o_id,m_id=m_id,money=money,m_way=m_way,remark=remark,discount=discount)
    db.add(new_receipt)
    db.commit()
    db.refresh(new_receipt)
    sum_,sum_1=sum_receipt_money(db=db,o_id=o_id,m_id=m_id)
    if sum_1-(0 if sum_==None else sum_)==0:
        od=db.query(models.order_new).filter(models.order_new.m_id==m_id,models.order_new.order_number==o_id)
        for i in od:
            i.pick_up_tf='是'
            db.commit() 
def sum_receipt_money(db:Session,o_id:int,m_id:int):
    return db.query(func.sum(models.receipt.money)).filter(models.receipt.o_id==o_id,models.receipt.m_id==m_id).scalar(),db.query(models.order_new).filter(models.order_new.order_number==o_id,models.order_new.m_id==m_id).first().total
def ac_get_od(db:Session,o_nb,m_id):
    return db.query(models.order_new).filter(models.order_new.order_number==o_nb,models.order_new.m_id==m_id)
def spilt_bill_pd(db:Session,id_:int):
    # mid=db.query(models.member).filter(models.member.Phone==phone).first().ID
    return db.query(models.order_list).filter(models.order_list.od_id==id_)
def spilt_bill_add(db:Session,phone:str,path:str,Pick_up:str,remark:str,product_:dict,date_:date,id_:int,discount:int):
    #刪除原本的產品 product_ {'產品':[數量,價錢]}
    try:
        for i in product_.keys():
            pid=db.query(models.product).filter(models.product.product_Name == i ).first().prodcut_ID
            od=db.query(models.order_list).filter(models.order_list.od_id==id_,models.order_list.p_id==pid).first()
            if (od.count-product_[i][0])==0:
                db.query(models.order_list).filter(models.order_list.od_id==id_,models.order_list.p_id==pid).delete()
                db.commit()
            else:
                od=db.query(models.order_list).filter(models.order_list.od_id==id_,models.order_list.p_id==pid).first()
                od.count-=product_[i][0]
                od.money=product_[i][1]
                db.commit()
        
        a=db.query(models.order_new).filter(models.order_new.id==id_).first()
        mid=a.m_id
        total_=int(db.query(func.sum(models.order_list.money)).filter(models.order_list.od_id==id_).first()[0])
        a.total=total_-a.discount
        db.commit()

        max_value=0
        if db.query(models.order_new).order_by(desc('order_number')).filter(models.order_new.id==id_).first()!=None:
            max_value=db.query(models.order_new).order_by(desc('order_number')).filter(models.order_new.id==id_).first().order_number
        su=sum(i[1] for i in product_.values())
        new=models.order_new(order_number=max_value+1,m_id=mid,pick_up=Pick_up,pick_up_tf='否',remark=remark,pick_up_date=date_,path=path,discount=discount,total=su-int(discount))
        db.add(new)
        db.commit()
        db.refresh(new)
        i=0
        for key,value in product_.items():
            pid=db.query(models.product).filter(models.product.product_Name == key ).first().prodcut_ID
            new_od=models.order_list(p_id=pid,od_id=new.id,count=value[0],money=value[1])         
            db.add(new_od)
            db.commit()
            db.refresh(new_od)
    except Exception as e:
        print(e)
        tk.messagebox.showinfo(title='失敗', message="請輸入電話", )
def date_search(db:Session,date1,date2):
    a=db.query(models.order_new).filter(models.order_new.pick_up_date.between(date1,date2))
    od_count=a.count()
    pd_count=0
    for i in a:
        pd_count+=sum(l.count for l in i.orders_)
    p_count=db.query(models.order_new.m_id).filter(models.order_new.pick_up_date.between(date1,date2)).distinct().count()
    sum_money,sum_discount=db.query(func.sum(models.order_new.total+models.order_new.discount),func.sum(models.order_new.discount)).filter(models.order_new.pick_up_date.between(date1,date2)).first()
    sum_profit=sum_money-sum_discount
    on_site_=db.query(models.order_new).filter(models.order_new.pick_up_date.between(date1,date2),models.order_new.pick_up=='現場')
    home_delivery_=db.query(models.order_new).filter(models.order_new.pick_up_date.between(date1,date2),models.order_new.pick_up=='宅配')
    p_on_site_=db.query(models.order_new).filter(models.order_new.pick_up_date.between(date1,date2),models.order_new.path=='現場')
    p_internet_=db.query(models.order_new).filter(models.order_new.pick_up_date.between(date1,date2),models.order_new.path=='網站')
    on_site=[0,0]
    home_delivery=[0,0]
    p_on_site=[0,0]
    p_internet=[0,0]
    for i in on_site_:
        on_site[0]+=sum(i.count for i in i.orders_)
        on_site[1]+=sum(i.money for i in i.orders_)
    for i in home_delivery_:
        home_delivery[0]+=sum(i.count for i in i.orders_)
        home_delivery[1]+=sum(i.money for i in i.orders_)
    for i in p_on_site_:
        p_on_site[0]+=sum(i.count for i in i.orders_)
        p_on_site[1]+=sum(i.money for i in i.orders_)
    for i in p_internet_:
        p_internet[0]+=sum(i.count for i in i.orders_)
        p_internet[1]+=sum(i.money for i in i.orders_)
    return od_count,pd_count,p_count,sum_money,sum_discount,sum_profit,on_site,home_delivery,p_on_site,p_internet
def pd_Analysis(db:Session,date1,date2):
    pd=db.query(models.product).all()
    pd_dict={}
    for i in pd:
        pd_dict[i.product_Name]=[0,0]
    pd_1=db.query(models.order_new).filter(models.order_new.pick_up_date.between(date1,date2))
    for i in pd_1:#[數量,價錢]
        for l in i.orders_:
            pd_dict[l.p_id_.product_Name][0]+=l.count
            pd_dict[l.p_id_.product_Name][1]+=l.money

    return pd_dict    
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