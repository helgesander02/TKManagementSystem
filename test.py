from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.crud import *
user=get_user(db=Session(engine),user_phone='0912345678')
for i in user.orders:
  print(i.order_number)
# order_list=search_od_(db=Session(engine),phone='phone',pick_up='pick_up',date_='2000/01/01',money1=1,money2=1111)

# try:
#             od_l={}
#             order_list=search_od_(db=Session(engine),phone='phone',pick_up='pick_up',date_='2000/01/01',money1=1,money2=1111)
#             for i in order_list:
#                 if i.order_number in od_l:
#                     od_l[i.order_number][4]+=f',{i.p_ID_.product_Name}'
#                     od_l[i.order_number][6]+=i.count*i.p_ID_.product_Price
#                 else:
#                     od_l[i.order_number]=[i.M_ID_.Name,i.od_id,i.pick_up_date,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.count*i.p_ID_.product_Price]
# except:
#             od_l={}
# print(od_l)
# a=get_user(Session(engine),'0912345678')
# print(a.Address)
# od_l={}
# a=get_od(Session(engine),'1')
# for i in a:
#   if i.order_number in od_l:
#       od_l[i.order_number][4]+=f',{i.p_ID_.product_Name}'
#       od_l[i.order_number][6]+=i.count*i.p_ID_.product_Price
#   else:
#       od_l[i.order_number]=[i.M_ID_.Name,i.od_id,i.Date_,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.count*i.p_ID_.product_Price]
# print(od_l)

# print(a.orders)
# for i in a.orders:
#   print(i.M_ID)
# od_nb=1
# b=[]
# for i in a:
#   if i.order_number==od_nb:
#     print(i.p_ID_.product_Name,end='')
#   else:
#     od_nb+=1
#     print()
#     print(i.p_ID_.product_Name,end='')

