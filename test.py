from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.crud import *
import pandas as pd
import os

# user=get_user(Session(engine),user_phone='0988635291')
# print(user.Address)
# print(user.orders)
# # try:
#     query = 'SELECT * FROM product'
#     df = pd.read_sql_query(query, engine)
#     for index, row in df.iterrows(): 
#         if row['content']==None:df.at[index, 'content'] = row['product_Name']    
#     print(df)         
# except:
#     print('a')
# mouse wheel scrolling with reduced speed
# def on_mouse_wheel(event):
#     canvas.yview('scroll', int(-1 * event.delta / 120), 'units')

# root = tk.Tk()
# root.bind('<MouseWheel>', on_mouse_wheel)  # bind mousewheel to root, this only works if you have a single scroll area
# window_width = 400
# window_height = 200
# table_columns = 4
# table_rows = 30

# root.geometry(f'{window_width}x{window_height}')

# main_frame = tk.Frame(root)
# main_frame.pack(fill=tk.BOTH, expand=1)  # frame goes to the left

# canvas = tk.Canvas(main_frame)
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# v_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
# v_scroll.pack(side=tk.RIGHT, fill=tk.Y)  # scrollbar goes to the right

# canvas.configure(yscrollcommand=v_scroll.set)
# canvas.bind(
#     '<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox(tk.ALL))
# )  # adjust scrolling area on resize

# inside_frame = tk.Frame(canvas)  # frame where you put your actual content
# canvas.create_window((0, 0), window=inside_frame, anchor=tk.N)  # adding the inside_frame to the canvas

# # an example grid with some data
# for y in range(table_rows):
#     for x in range(table_columns):
#         tk.Label(inside_frame, text=f'{y}:{x}', borderwidth=1, relief=tk.SOLID, width=10).grid(column=x, row=y)
        
# root.mainloop()
# order_list=search_od_(db=Session(engine),phone='phone',pick_up='pick_up',date_='2000/01/01',money1=1,money2=1111)

# try:
#             od_l={}
#             order_list=search_od_(db=Session(engine),phone='phone',pick_up='pick_up',date_='2000/01/01',money1=1,money2=1111)
#             for i in order_list:
#                 if i.order_number in od_l:
#                     od_l[i.order_number][4]+=f',{i.p_ID_.product_Name}'
#                     od_l[i.order_number][6]+=i.count*i.p_ID_.product_Price
#                 else:
#                     od_l[i.order_number]=[i.M_ID_.Phone,i.od_id,i.pick_up_date,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.count*i.p_ID_.product_Price]
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

