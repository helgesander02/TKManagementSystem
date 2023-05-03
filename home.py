#-*- coding: utf-8 -*-
import tkinter as tk
import customtkinter

from order import Order_Main_Frame
from menber import Menber_Main_Frame
from goods import Goods_Main_Frame
from data import Data_Main_Frame

from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine,SessionLocal

# https://steam.oxxostudio.tw/category/python/tkinter/grid.html
# .grid 詳細解釋
# https://vocus.cc/article/62577184fd89780001e55c39
# .pack, .place, .grid 詳細解釋
# https://steam.oxxostudio.tw/category/python/tkinter/index.html
# Tkinter 教學

# Select_Frame 選單按鈕
class Select_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.btn_home = customtkinter.CTkButton(self ,text="home" ,width=160 ,height=160 ,
                                                                fg_color=("#5b5a5a"),corner_radius=0)
        self.btn_home.grid(row=0, column=0)

        self.btn_order = customtkinter.CTkButton(self ,text="Order" ,width=160 ,height=160 ,
                                                                fg_color=("#5b5a5a"),corner_radius=0)
        self.btn_order.grid(row=1, column=0)

        self.btn_menber = customtkinter.CTkButton(self ,text="Menber" ,width=160 ,height=160 ,
                                                                fg_color=("#5b5a5a"),corner_radius=0)
        self.btn_menber.grid(row=2, column=0)

        self.btn_goods = customtkinter.CTkButton(self ,text="Goods" ,width=160 ,height=160 ,
                                                                fg_color=("#5b5a5a"),corner_radius=0)
        self.btn_goods.grid(row=3, column=0)

        self.btn_data = customtkinter.CTkButton(self ,text="Data" ,width=160 ,height=160 ,
                                                                fg_color=("#5b5a5a"),corner_radius=0)
        self.btn_data.grid(row=4, column=0)

        self.btn_other = customtkinter.CTkButton(self ,text="" ,width=160 ,height=160 ,
                                                                fg_color=("#5b5a5a"),corner_radius=0)
        self.btn_other.grid(row=5, column=0)
    def reset_(self):
        self.btn_home.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_order.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_menber.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_goods.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_data.configure(fg_color = "#5b5a5a",text_color='white')
        self.btn_other.configure(fg_color = "#5b5a5a",text_color='white')
# Home_Main_Frame (Search_Frame, Schedule_Frame) 主頁
class Search_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #會員查詢
        # #relx/rely range[0.0, 1,0]
        self.MS_label = customtkinter.CTkLabel(self, text="會員查詢" ,font=("microsoft yahei", 35, 'bold'),text_color='black')
        self.MS_label.place(relx=0.1, rely=0.5, anchor=tk.CENTER)
        
        self.MS_entry = customtkinter.CTkEntry(self, width=250, height=40, 
                                                        border_width=3,
                                                        border_color=("#5b5a5a"), 
                                                        fg_color=("#DDDDDD"),
                                                        text_color='black')

        self.MS_entry.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        
        self.MS_button = customtkinter.CTkButton(self, text="Q", width=40, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'))

        self.MS_button.place(relx=0.42, rely=0.5, anchor=tk.CENTER)

        #顯示是否有此會員
        self.tf_label = customtkinter.CTkLabel(self, text="")
        self.tf_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #2個按鈕
        self.order_button = customtkinter.CTkButton(self, text="新增訂單", width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'))

        self.order_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

        self.menber_button = customtkinter.CTkButton(self, text="新增會員", width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'))

        self.menber_button.place(relx=0.9, rely=0.5, anchor=tk.CENTER)
    
class Schedule_Frame(customtkinter.CTkFrame):
    def __init__(self, master,user_name, **kwargs):
        super().__init__(master, **kwargs)

        for i in range(7):
            self.columnconfigure(i,weight=1)
        self.columnconfigure(4,weight=2)
        a=customtkinter.CTkLabel(self,text='會員資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=0)
        a=customtkinter.CTkLabel(self,text='訂單資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=1)
        a=customtkinter.CTkLabel(self,text='取貨日期',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=2) 
        a=customtkinter.CTkLabel(self,text='取貨方式',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=3) 
        a=customtkinter.CTkLabel(self,text='訂單項目',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=4)
        a=customtkinter.CTkLabel(self,text='是否取貨',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=5)
        a=customtkinter.CTkLabel(self,text='金額',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=6)
        if user_name!='':
            user=get_user(Session(engine),user_name)
            od_l={}
            order_list=get_od(Session(engine),user_id=user.ID)
            for i in order_list:
                if i.order_number in od_l:
                    od_l[i.order_number][4]+=f',{i.p_ID_.product_Name}'
                    od_l[i.order_number][6]+=i.count*i.p_ID_.product_Price
                else:
                    od_l[i.order_number]=[i.M_ID_.Name,i.od_id,i.Date_,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.count*i.p_ID_.product_Price]
            for key,value in od_l.items():
                a=customtkinter.CTkLabel(self,text=f'{key}',fg_color = ("#DDDDDD"),text_color='black')
                a.grid(row=key,column=0)
                a=customtkinter.CTkLabel(self,text=f'{value[1]}',fg_color = ("#DDDDDD"),text_color='black')
                a.grid(row=key,column=1)
                a=customtkinter.CTkLabel(self,text=f'{value[2]}',fg_color = ("#DDDDDD"),text_color='black')
                a.grid(row=key,column=2) 
                a=customtkinter.CTkLabel(self,text=f'{value[3]}',fg_color = ("#DDDDDD"),text_color='black')
                a.grid(row=key,column=3) 
                a=customtkinter.CTkLabel(self,text=f'{value[4]}',fg_color = ("#DDDDDD"),text_color='black')
                a.grid(row=key,column=4,sticky='w')
                a=customtkinter.CTkLabel(self,text=f'{value[5]}',fg_color = ("#DDDDDD"),text_color='black')
                a.grid(row=key,column=5)
                a=customtkinter.CTkLabel(self,text=f'{value[6]}',fg_color = ("#DDDDDD"),text_color='black')
                a.grid(row=key,column=6)
class Home_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #Search_Frame
        self.Search_Frame_ = Search_Frame(self,  fg_color = ("#DDDDDD"))
        self.Search_Frame_.MS_button.configure(command=lambda: self.search_user(self.Search_Frame_.MS_entry.get()))
        self.Search_Frame_.pack(pady=30,padx=30,fill='x')
        
        #Schedule_Frame
        self.Schedule_Frame_ = Schedule_Frame(self,user_name='',  fg_color = ("#DDDDDD"))
        
        self.Schedule_Frame_.pack(fill='both',expand=1,padx=30,pady=30)
        
    def search_user(self,user_name):
        self.Schedule_Frame_.pack_forget()
        self.Schedule_Frame_=Schedule_Frame(self,user_name=user_name,  fg_color = ("#DDDDDD"))
        self.Schedule_Frame_.pack(fill='both',expand=1,padx=30,pady=30)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Define System  
        width = 1440
        height = 960
        self.geometry(f'{width}x{height}+{int((self.winfo_screenwidth() - width)/2)}+{int((self.winfo_screenheight() - height)/2)}')
        self.title("美而香管理系統")
        customtkinter.set_appearance_mode("light")
        #Define Home
        #Select_Frame
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1) 
        self.Select_Frame = Select_Frame(self,  fg_color = ("#5b5a5a"))
        self.Select_Frame.grid(row=0, column=0,sticky='nsew')
        #Main_Frame
        self.Main_Frame = Home_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
        self.Main_Frame.grid(row=0, column=1,sticky='nsew')

        #關掉主要的Frame開啟對應btn的Frame
        #隱藏的方法 https://www.delftstack.com/zh-tw/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/
        def open_home (event):   
            self.Main_Frame.grid_forget()
            self.Select_Frame.reset_()
            self.Select_Frame.btn_home.configure(fg_color = "#EEEEEE",text_color='black')
            self.Main_Frame = Home_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            self.Main_Frame.grid(row=0, column=1,sticky='nsew')

        def open_order (event):
            self.Main_Frame.grid_forget()
            self.Select_Frame.reset_()
            self.Select_Frame.btn_order.configure(fg_color = "#EEEEEE",text_color='black')
            self.Main_Frame = Order_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0)
            self.Main_Frame.grid(row=0, column=1,sticky='nsew')

        def open_menber (event):
            self.Main_Frame.grid_forget()
            self.Select_Frame.reset_()
            self.Select_Frame.btn_menber.configure(fg_color = "#EEEEEE",text_color='black')
            self.Main_Frame = Menber_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            self.Main_Frame.grid(row=0, column=1,sticky='nsew')

        def open_goods (event):
            self.Main_Frame.grid_forget()
            self.Select_Frame.reset_()
            self.Select_Frame.btn_goods.configure(fg_color = "#EEEEEE",text_color='black')
            self.Main_Frame = Goods_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            self.Main_Frame.grid(row=0, column=1,sticky='nsew')

        def open_data (event):
            self.Main_Frame.grid_forget()
            self.Select_Frame.reset_()
            self.Select_Frame.btn_data.configure(fg_color = "#EEEEEE",text_color='black')
            self.Main_Frame = Data_Main_Frame(self,  fg_color = ("#EEEEEE"), corner_radius=0 )
            self.Main_Frame.grid(row=0, column=1,sticky='nsew')

        def clear_main (event):
            self.Main_Frame.grid_forget()

        #切換功能
        #btn事件教學 https://ithelp.ithome.com.tw/articles/10275712?sc=iThomeR
        self.Select_Frame.btn_home.bind("<Button-1>", open_home)
        self.Select_Frame.btn_order.bind("<Button-1>", open_order)
        self.Select_Frame.btn_menber.bind("<Button-1>", open_menber)
        self.Select_Frame.btn_goods.bind("<Button-1>", open_goods)
        self.Select_Frame.btn_data.bind("<Button-1>", open_data)

app = App()
app.mainloop()