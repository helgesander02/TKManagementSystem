#-*- coding: utf-8 -*-
import tkinter as tk
import customtkinter
from tkcalendar import DateEntry
import customtkinter as ctk
from typing import Union
from typing import Callable
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine,SessionLocal
from tkinter import *
from PIL import Image, ImageTk
# Order () 訂單
phone_data=''
pick_up_data=''
remark_data=''
class Order_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bt_frame=button_Frame(self,  fg_color = ("#EEEEEE") ,)
        self.bt_frame.pack(pady=40,padx=40,anchor='nw')
        self.input_order_=input_order(self,  fg_color = ("#DDDDDD"))
        self.input_order_.pack(fill='both',expand=1,padx=40,pady=40,anchor='nw')
        self.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
        def input_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.input_order_.pack_forget()
            self.input_order_=input_order(self,  fg_color = ("#DDDDDD"))
            self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        def edit_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.edit_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.input_order_.pack_forget()
            self.input_order_=edit_order(self,  fg_color = ("#DDDDDD") )
            self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        def finish_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.finish_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.input_order_.pack_forget()
            self.input_order_=finish_frame(self,  fg_color = ("#DDDDDD"))
            self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        self.bt_frame.input_button.bind("<Button-1>", input_button_click)
        self.bt_frame.edit_button.bind("<Button-1>", edit_button_click)
        self.bt_frame.finish_button.bind("<Button-1>", finish_button_click)
        def bt():
            print('s')
class edit_order(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # self.edit_top_=edit_top(self,fg_color = ("#DDDDDD"))
        self.edit_top_=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(7):
            self.edit_top_.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.edit_top_, text="電話",text_color='black')
        self.phone=customtkinter.CTkEntry(self.edit_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black')
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.edit_top_, text="通路",text_color='black')
        self.path=customtkinter.CTkComboBox(self.edit_top_,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.edit_top_, text="取貨方式",text_color='black')
        self.pick_up=customtkinter.CTkComboBox(self.edit_top_,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.edit_top_, text="日期",text_color='black')
        self.date_=DateEntry(self.edit_top_,selectmode='day')
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.money_label=customtkinter.CTkLabel(self.edit_top_, text="金額",text_color='black')
        self.money=customtkinter.CTkEntry(self.edit_top_, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black')
        self.money2=customtkinter.CTkEntry(self.edit_top_, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black')
        self.money_label.grid(row=0,column=4,padx=30,pady=5)
        self.money.grid(row=0,column=5,padx=30,pady=5)
        self.money2.grid(row=1,column=5,padx=30,pady=5)
        reset_bt=customtkinter.CTkButton(self.edit_top_,text='重新設定', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        )
        reset_bt.grid(row=0,column=6,padx=30,pady=5)
        search=customtkinter.CTkButton(self.edit_top_,text='確定查詢', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        command=lambda: self.search_od_list(phone=self.phone.get(),pick_up=self.pick_up.get(),date_=self.date_.get_date(),money1=self.money.get(),money2=self.money2.get()))
        search.grid(row=1,column=6,padx=30,pady=5)  
     
        self.edit_top_.pack(fill='x',padx=30,pady=5)
        self.ol=order_List(self,phone='',pick_up='',date_='',money1='',money2='',fg_color = ("#DDDDDD"))
        self.ol.pack(fill='x',padx=30,pady=5)
    def search_od_list(self,phone,pick_up,date_,money1,money2):
        self.ol.pack_forget()
        self.ol=order_List(self,phone=phone,pick_up=pick_up,date_=date_,money1=money1,money2=money2,fg_color = ("#DDDDDD"))
        self.ol.pack(fill='x',padx=30,pady=5)
    def delete_(self):
        pass
class finish_frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.search=finish_search_fame(self,fg_color = ("#DDDDDD"))
        self.search.pack(fill='both',side='left',expand=1,padx=15,pady=5)
        # search1=finish_frame2(self,fg_color = ("#DDDDDD"))
        # search1.pack(fill='both',side='left',expand=1,padx=15,pady=5)       
class finish_search_fame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.toplevel_window = None
        a=customtkinter.CTkFrame(self,fg_color=("#DDDDDD"))
        search_label=customtkinter.CTkLabel(a,text='訂單查詢',fg_color = ("#DDDDDD"),text_color='black')
        # search_label.grid(row=0,column=0,padx=30,pady=5,sticky='ew')
        search_label.pack(side='left')
        self.search=customtkinter.CTkEntry(a,fg_color = ("#DDDDDD"),text_color='black')
        self.search_bt=customtkinter.CTkButton(a, text="Q", width=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'),
                                                        command=self.search_A)
        self.search.pack(side='left')
        self.search_bt.pack(side='left')
        a.pack(anchor='n',fill='x',padx=30,pady=5)
        
        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='廠商資訊',text_color='black')
        order_n1=customtkinter.CTkLabel(self.history_frame,text='訂單內容',text_color='black')
        order_n2=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black')
        order_n3=customtkinter.CTkLabel(self.history_frame,text='',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        self.toplevel_window = None
        self.history_frame.pack(fill='x',anchor='n',pady=40,padx=30)
    def search_A(self):
        try:
            self.od_l={}
            user=get_user(Session(engine),user_phone=self.search.get())
            for i in user.orders:
                if i.order_number in self.od_l:
                    self.od_l[i.order_number][1]+=f',{i.p_ID_.product_Name}'
                else:
                    self.od_l[i.order_number]=[i.M_ID_.ID,i.p_ID_.product_Name,i.money]
        except:
            self.od_l={}        
        self.history_frame.pack_forget()
        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='廠商資訊',text_color='black')
        order_n1=customtkinter.CTkLabel(self.history_frame,text='訂單內容',text_color='black')
        order_n2=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black')
        order_n3=customtkinter.CTkLabel(self.history_frame,text='',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        
        self.history_frame.pack(fill='x',anchor='n',pady=40,padx=30)
        l=1
        def gen_cmd(i,l):return lambda:self.update_(i,l)
        for key,value in self.od_l.items():
            order_n=customtkinter.CTkLabel(self.history_frame,text=f'{value[0]}',text_color='black')
            order_n1=customtkinter.CTkLabel(self.history_frame,text=f'{value[1]}',text_color='black')
            order_n2=customtkinter.CTkLabel(self.history_frame,text=f'{value[2]}',text_color='black')
            order_n4=customtkinter.CTkButton(self.history_frame,text='確認入賬',text_color='black',command=gen_cmd(key,value[0]))
            order_n.grid(row=l,column=0,sticky='w')
            order_n1.grid(row=l,column=1,sticky='w')
            order_n2.grid(row=l,column=2)
            order_n4.grid(row=l,column=3)
            l+=1
    def update_(self,key,m_id):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = cm_ToplevelWindow(self,key=key,m_id=m_id)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus() 
class cm_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,key,m_id, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        self.key=key
        self.m_id=m_id
        edit_n=customtkinter.CTkLabel(self,text='剩餘金額',text_color='black')
        edit_n1=customtkinter.CTkLabel(self,text='入帳金額',text_color='black')
        money=customtkinter.CTkLabel(self,text=f'{get_balance(db=Session(engine),od_nb=key,m_id=m_id)}')
        self.edit_entry_n=customtkinter.CTkEntry(self)
        self.cancel_bt=customtkinter.CTkButton(self,text='取消',command=self.cancel_click)
        confirm_bt=customtkinter.CTkButton(self,text='確定入賬',command=self.confirm_edit)
        self.cancel_bt.grid(row=3,column=0,sticky='e',padx=30,pady=10)
        confirm_bt.grid(row=3,column=1,sticky='e',padx=30,pady=10)
        edit_n.grid(row=1,column=0)
        edit_n1.grid(row=2,column=0)
        self.edit_entry_n.grid(row=2,column=1,sticky='ew',padx=10,pady=10)
        money.grid(row=1,column=1)
    def cancel_click(self):
        self.destroy()
    def confirm_edit(self):
        try:
            update_balance(db=Session(engine),od_nb=self.key,m_id=self.m_id,cm=self.edit_entry_n.get())
            tk.messagebox.showinfo(title='入賬成功', message="入賬成功", )
            self.destroy()
        except:
            tk.messagebox.showinfo(title='入賬失敗', message="入賬失敗", )
class order_List(customtkinter.CTkFrame):
    def __init__(self, master,phone,pick_up,date_,money1,money2, **kwargs):
        super().__init__(master, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open("image\\user.png"),
                                  dark_image=Image.open("image\\user.png"),
                                  size=(30, 30))
        self.info = customtkinter.CTkImage(light_image=Image.open("image\\information-button.png"),
                                  dark_image=Image.open("image\\information-button.png"),
                                  size=(30, 30))
        self.edit_photo = customtkinter.CTkImage(light_image=Image.open("image\\pencil.png"),
                                  dark_image=Image.open("image\\pencil.png"),
                                  size=(30, 30))
        self.delete_photo = customtkinter.CTkImage(light_image=Image.open("image\\close.png"),
                                  dark_image=Image.open("image\\close.png"),
                                  size=(30, 30))        
        try:
            self.od_l={}
            order_list=search_od_(db=Session(engine),phone=phone,pick_up=pick_up,date_=date_,money1=money1,money2=money2)
            for i in order_list:
                if i.order_number in self.od_l:
                    self.od_l[i.order_number][4]+=f',{i.p_ID_.product_Name}'
                    self.od_l[i.order_number][6]+=i.count*i.p_ID_.product_Price
                else:
                    self.od_l[i.order_number]=[i.M_ID_.Phone,i.od_id,i.pick_up_date,i.pick_up,i.p_ID_.product_Name,i.pick_up_tf,i.count*i.p_ID_.product_Price]
        except:
            self.od_l={}
        self.c=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(9):
            self.c.columnconfigure(i,weight=1)
        self.c.columnconfigure(4,weight=2)
        a=customtkinter.CTkLabel(self.c,text='會員資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=0)
        a=customtkinter.CTkLabel(self.c,text='訂單資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=1)
        a=customtkinter.CTkLabel(self.c,text='取貨日期',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=2) 
        a=customtkinter.CTkLabel(self.c,text='取貨方式',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=3) 
        a=customtkinter.CTkLabel(self.c,text='訂單項目',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=4)
        a=customtkinter.CTkLabel(self.c,text='是否取貨',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=5)
        a=customtkinter.CTkLabel(self.c,text='金額',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=6)
        a=customtkinter.CTkLabel(self.c,text='編輯',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=7)
        a=customtkinter.CTkLabel(self.c,text='刪除',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=8)
        
        i=1
        def gen_cmd1(i,l):return lambda:self.edit_(i,l)
        def gen_cmd(i):return lambda:self.delete(i)
        def get_user(i):return lambda:self.get_u(i)
        def get_od_(i):return lambda:self.get_o(i)
        for key,value in self.od_l.items():
            a=customtkinter.CTkButton(self.c,image=self.image,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_user(value[0]))
            # a=customtkinter.CTkLabel(self.c,text=f'{value[0]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=0)
            a=customtkinter.CTkButton(self.c,image=self.info,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_od_(value[1]))
            a.grid(row=i,column=1)
            a=customtkinter.CTkLabel(self.c,text=f'{value[2]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=2) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[3]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=3) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[4]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=4)
            a=customtkinter.CTkLabel(self.c,text=f'{value[5]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=5)
            a=customtkinter.CTkLabel(self.c,text=f'{value[6]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=6)
            a=customtkinter.CTkButton(self.c,image=self.edit_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd1(key,value[0]))
            a.grid(row=i,column=7)
            a=customtkinter.CTkButton(self.c,image=self.delete_photo,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd(key))
            a.grid(row=i,column=8)
            i+=1
        self.c.pack(fill='x')
        self.toplevel_window = None
    def get_o(self,i):
        
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = info_ToplevelWindow(self,od=i)  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus() 
    def get_u(self,i):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = profile_ToplevelWindow(self,phone=i)  
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()        
    def edit_(self,i,l):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = edit_ToplevelWindow(self,key=i,M_Name=l)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()        
    def delete(self,i):
        delete_od(Session(engine),i)
        del self.od_l[i]
        self.c.pack_forget()
        self.c=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(9):
            self.c.columnconfigure(i,weight=1)
        self.c.columnconfigure(4,weight=2)
        a=customtkinter.CTkLabel(self.c,text='會員資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=0)
        a=customtkinter.CTkLabel(self.c,text='訂單資訊',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=1)
        a=customtkinter.CTkLabel(self.c,text='取貨日期',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=2) 
        a=customtkinter.CTkLabel(self.c,text='取貨方式',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=3) 
        a=customtkinter.CTkLabel(self.c,text='訂單項目',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=4)
        a=customtkinter.CTkLabel(self.c,text='是否取貨',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=5)
        a=customtkinter.CTkLabel(self.c,text='金額',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=6)
        a=customtkinter.CTkLabel(self.c,text='編輯',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=7)
        a=customtkinter.CTkLabel(self.c,text='刪除',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=8)
        
        i=1
        def gen_cmd1(i,l):return lambda:self.edit_(i,l)
        def gen_cmd(i):return lambda:self.delete(i)
        def get_user(i):return lambda:self.get_u(i)
        def get_od_(i):return lambda:self.get_o(i)
        for key,value in self.od_l.items():
            a=customtkinter.CTkButton(self.c,image=self.image,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_user(value[0]))
            a.grid(row=i,column=0)
            a=customtkinter.CTkButton(self.c,image=self.info,hover=False,text='',fg_color = ("#DDDDDD"),text_color='black',command=get_od_(value[1]))
            a.grid(row=i,column=1)
            a=customtkinter.CTkLabel(self.c,text=f'{value[2]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=2) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[3]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=3) 
            a=customtkinter.CTkLabel(self.c,text=f'{value[4]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=4)
            a=customtkinter.CTkLabel(self.c,text=f'{value[5]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=5)
            a=customtkinter.CTkLabel(self.c,text=f'{value[6]}',fg_color = ("#DDDDDD"),text_color='black')
            a.grid(row=i,column=6)
            a=customtkinter.CTkButton(self.c,text='編輯',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd1(key,value[0]))
            a.grid(row=i,column=7)
            a=customtkinter.CTkButton(self.c,text='刪除',fg_color = ("#DDDDDD"),text_color='black',command=gen_cmd(key))
            a.grid(row=i,column=8)
            i+=1
        self.c.pack(fill='x')
class info_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,od, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open("image\\user.png"),
                                  dark_image=Image.open("image\\user.png"),
                                  size=(100, 100))
        self.geometry("400x500")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        
        od_=get_od_info(Session(engine),od_nb=od)    
        edit_n=customtkinter.CTkLabel(self,text='訂單編號：',text_color='black')
        edit_n1=customtkinter.CTkLabel(self,text='通路：',text_color='black')
        edit_n2=customtkinter.CTkLabel(self,text='備註：',text_color='black')
        
        # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
        edit_nL=customtkinter.CTkLabel(self,text=f'{od_.od_id}',text_color='black')
        edit_n1L=customtkinter.CTkLabel(self,text=f'{od_.pick_up}',text_color='black')
        edit_n2L=customtkinter.CTkLabel(self,text=f'{od_.Remark}',text_color='black')
        
        bt.grid(row=0,column=0,columnspan=2,pady=20)
        edit_n.grid(row=1,column=0)#姓名
        edit_n1.grid(row=2,column=0)#電話
        edit_n2.grid(row=3,column=0)#地址
        
        
        edit_nL.grid(row=1,column=1)#姓名
        edit_n1L.grid(row=2,column=1)#電話
        edit_n2L.grid(row=3,column=1)#地址
         
class profile_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,phone, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = customtkinter.CTkImage(light_image=Image.open("image\\user.png"),
                                  dark_image=Image.open("image\\user.png"),
                                  size=(100, 100))
        self.geometry("400x500")
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((3,4),weight=2)
        bt=customtkinter.CTkLabel(self,image=self.image,text='')
        user=get_user(db=Session(engine),user_phone=phone)    
        edit_n=customtkinter.CTkLabel(self,text='會員編號：',text_color='black')
        edit_n1=customtkinter.CTkLabel(self,text='會員姓名：',text_color='black')
        edit_n2=customtkinter.CTkLabel(self,text='地址：',text_color='black')
        edit_n3=customtkinter.CTkLabel(self,text='備註：',text_color='black')
        # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
        edit_nL=customtkinter.CTkLabel(self,text=f'{user.ID}',text_color='black')
        edit_n1L=customtkinter.CTkLabel(self,text=f'{user.Name}',text_color='black')
        edit_n2L=customtkinter.CTkLabel(self,text=f'{user.Address}',text_color='black')
        edit_n3L=customtkinter.CTkLabel(self,text=f'{user.Remark}',text_color='black')
        bt.grid(row=0,column=0,columnspan=2,pady=20)
        edit_n.grid(row=1,column=0)#姓名
        edit_n1.grid(row=2,column=0)#電話
        edit_n2.grid(row=3,column=0)#地址
        edit_n3.grid(row=4,column=0)#備註
        
        edit_nL.grid(row=1,column=1)#姓名
        edit_n1L.grid(row=2,column=1)#電話
        edit_n2L.grid(row=3,column=1)#地址
        edit_n3L.grid(row=4,column=1)#備註          
class edit_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,key,M_Name, **kwargs):
        super().__init__(*args, **kwargs)
        self.buy_photo = customtkinter.CTkImage(light_image=Image.open("image\\cart.png"),
                                  dark_image=Image.open("image\\cart.png"),
                                  size=(30, 30))        
        od=get_edit_od(Session(engine),key,M_Name)
        self.key=key
        self.M_Name=M_Name
        self.geometry("1000x900")
        self.columnconfigure((0,1),weight=1)
        self.input_top_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        self.input_top_.columnconfigure(5,weight=5)
        for i in range(6):
            self.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.input_top_, text="電話",text_color='black')
        self.phone=customtkinter.CTkEntry(self.input_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black')
        self.phone.insert(END,'' if od[0].phone==None else od[0].phone)
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.input_top_, text="通路",text_color='black')
        self.path=customtkinter.CTkComboBox(self.input_top_,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.input_top_, text="取貨方式",text_color='black')
        self.pick_up=customtkinter.CTkComboBox(self.input_top_,values=["現場", "取貨2"],fg_color = ("#DDDDDD"),text_color='black')
        self.pick_up.set(od[0].pick_up)
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.input_top_, text="取貨日期",text_color='black')
        self.date_=DateEntry(self.input_top_,selectmode='day')
        self.date_.set_date(od[0].pick_up_date)
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.Remark_label=customtkinter.CTkLabel(self.input_top_, text="備註",text_color='black')
        self.Remark_label.grid(row=0,column=4,padx=30,pady=5)
        self.Remark_textbox = customtkinter.CTkTextbox(self.input_top_, corner_radius=0,fg_color='white',border_color='black',text_color='black',border_width=1)
        self.Remark_textbox.insert(END,'' if od[0].Remark==None else od[0].Remark)
        self.Remark_textbox.grid(row=0, column=5,rowspan=3,padx=30,pady=5,sticky='we')        
        # self.input_top_=input_top(self, fg_color = ("#DDDDDD")) 
        self.input_top_.pack(fill='x',padx=30,pady=5)
        
        self.product_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        prodcuts=get_all_products(Session(engine))
        self.toplevel_window = None
        self.bt_group={}
        self.buy_list={}
        for i in od:
            self.buy_list[i.p_ID_.product_Name]=[i.count,i.p_ID_.product_Price]
        self.a_frame=customtkinter.CTkFrame(self.product_,fg_color = ("#DDDDDD"))
        for i in range(len(prodcuts)):
            self.a_frame.columnconfigure(i,weight=1)
        def gen_cmd(i):return lambda:self.buy_bt_click(i)
        for i in range(len(prodcuts)):
            label_Name=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Name,text_color='black')
            label_Name.grid(row=i,column=0,padx=30,sticky='w')
            label_Weight=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Weight,text_color='black')
            label_Weight.grid(row=i,column=1,padx=30)
            label_price=customtkinter.CTkLabel(self.a_frame,text=f'{prodcuts[i].product_Price}元',text_color='black')
            label_price.grid(row=i,column=2,padx=30)
            
            spinbox_1 = FloatSpinbox(self.a_frame, width=150, step_size=1)
            self.bt_group[prodcuts[i].product_Name]=[spinbox_1,prodcuts[i].product_Price]
            spinbox_1.grid(row=i,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,  fg_color = ("#DDDDDD"), text="",command=gen_cmd(prodcuts[i].product_Name))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
            
        self.a_frame.pack(side='left',anchor='n',fill='x',expand=1)
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')        
        # self.product_=product_Frame(self, fg_color = ("#DDDDDD"))
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
    def add_od(self):
        edit_order_(db=Session(engine),phone=self.phone.get(),Pick_up=self.pick_up.get(),remark=self.Remark_textbox.get(1.0,'end'),product_=self.buy_list,m_id='1',date_=self.date_.get_date(),key=self.key,M_name=self.M_Name)
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
        self.destroy()
    def buy_bt_click(self,a):
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a=a,buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
        self.buy_list=self.sum_frame_.buy_list   
    def reset_(self):
        self.buy_list={}
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')         
class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #5b5a5a
        self.input_button = customtkinter.CTkButton(self, text="輸入訂單", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.input_button.grid(row=0, column=5,padx=30)
        self.edit_button = customtkinter.CTkButton(self, text="編輯與查詢", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.edit_button.grid(row=0, column=6,padx=30)

        self.finish_button = customtkinter.CTkButton(self, text="完成訂單", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.finish_button.grid(row=0, column=7,padx=30)
    def reset_color(self):
        self.input_button.configure(fg_color = ("#EEEEEE"),text_color='black')
        self.edit_button.configure(fg_color = ("#EEEEEE"),text_color='black')
        self.finish_button.configure(fg_color = ("#EEEEEE"),text_color='black')
class input_order(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.buy_photo = customtkinter.CTkImage(light_image=Image.open("image\\cart.png"),
                                  dark_image=Image.open("image\\cart.png"),
                                  size=(30, 30))
        self.columnconfigure((0,1),weight=1)
        self.input_top_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        self.input_top_.columnconfigure(5,weight=5)
        for i in range(6):
            self.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self.input_top_, text="電話",text_color='black')
        self.phone=customtkinter.CTkEntry(self.input_top_, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black')
        
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self.input_top_, text="通路",text_color='black')
        self.path=customtkinter.CTkComboBox(self.input_top_,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self.input_top_, text="取貨方式",text_color='black')
        self.pick_up=customtkinter.CTkComboBox(self.input_top_,values=["現場", "取貨2"],fg_color = ("#DDDDDD"),text_color='black')
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self.input_top_, text="取貨日期",text_color='black')
        self.date_=DateEntry(self.input_top_,selectmode='day')
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.Remark_label=customtkinter.CTkLabel(self.input_top_, text="備註",text_color='black')
        self.Remark_label.grid(row=0,column=4,padx=30,pady=5)
        self.Remark_textbox = customtkinter.CTkTextbox(self.input_top_, corner_radius=0,fg_color='white',border_color='black',text_color='black',border_width=1)
        self.Remark_textbox.grid(row=0, column=5,rowspan=3,padx=30,pady=5,sticky='we')        
        # self.input_top_=input_top(self, fg_color = ("#DDDDDD")) 
        self.input_top_.pack(fill='x',padx=30,pady=5)
        
        
        self.product_=customtkinter.CTkFrame(self, fg_color = ("#DDDDDD"))
        prodcuts=get_all_products(Session(engine))
        self.toplevel_window = None
        self.bt_group={}
        self.buy_list={}
        self.a_frame=customtkinter.CTkFrame(self.product_,fg_color = ("#DDDDDD"))
        
        for i in range(len(prodcuts)):
            self.a_frame.columnconfigure(i,weight=1)
        def gen_cmd(i):return lambda:self.buy_bt_click(i)
        for i in range(len(prodcuts)):
            label_Name=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Name,text_color='black')
            label_Name.grid(row=i,column=0,padx=30,sticky='w')
            label_Weight=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Weight,text_color='black')
            label_Weight.grid(row=i,column=1,padx=30)
            label_price=customtkinter.CTkLabel(self.a_frame,text=f'{prodcuts[i].product_Price}元',text_color='black')
            label_price.grid(row=i,column=2,padx=30)
            
            spinbox_1 = FloatSpinbox(self.a_frame, width=150, step_size=1)
            self.bt_group[prodcuts[i].product_Name]=[spinbox_1,prodcuts[i].product_Price]
            spinbox_1.grid(row=i,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo,hover=False,fg_color = ("#DDDDDD"), text="",command=gen_cmd(prodcuts[i].product_Name))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
            
        self.a_frame.pack(side='left',anchor='n',fill='x',expand=1)
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        # self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')        
        # self.product_=product_Frame(self, fg_color = ("#DDDDDD"))
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
    def add_od(self):
        try:
            add_order(db=Session(engine),phone=self.phone.get(),Pick_up=self.pick_up.get(),remark=self.Remark_textbox.get(1.0,'end'),product_=self.buy_list,m_id='1',date_=self.date_.get_date())
            self.sum_frame_.pack_forget()
            self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
            self.sum_frame_.reset_bt.configure(command=self.reset_)
            self.sum_frame_.pack(side='right',anchor='n',fill='both')
            tk.messagebox.showinfo(title='新增成功', message="新增成功", )            
        except:
            tk.messagebox.showinfo(title='新增失敗', message="新增失敗", )
    def buy_bt_click(self,a):
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a=a,buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
        self.buy_list=self.sum_frame_.buy_list
        
    def reset_(self):
        self.buy_list={}
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
# https://gist.github.com/apua/e43f007fbc9813ae97f7831ed25bb62b
class sum_Frame(customtkinter.CTkFrame):
    def __init__(self, master,a,buy_list,bt_group, **kwargs):
        super().__init__(master, **kwargs)
        self.a=a
        self.buy_list=buy_list
        self.bt_group=bt_group
        # self.contents_=sum_list(self,a=self.a,buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        # self.contents_.pack(fill='both',expand=1)
        self.contents_=customtkinter.CTkFrame(self,  fg_color = ("#EEEEEE"))
        self.contents_.rowconfigure(len(buy_list),weight=1)
        
        if self.a!='':
            self.buy_list[self.a]=[self.bt_group[self.a][0].get(),self.bt_group[self.a][1]]
            if self.buy_list[self.a][0]==0:del self.buy_list[self.a]
        i=0
        for key,value in self.buy_list.items():
            name_=customtkinter.CTkLabel(self.contents_,text=f'{key}',text_color='black')
            number_=customtkinter.CTkLabel(self.contents_,text=f'X{value[0]:5}',text_color='black')
            price_=customtkinter.CTkLabel(self.contents_,text=f'{value[0]*value[1]}',text_color='black')
            name_.grid(row=i,column=0, padx=20, pady=3,sticky='nw')
            number_.grid(row=i,column=1, padx=20, pady=3,sticky='n')
            price_.grid(row=i,column=2, padx=20, pady=3,sticky='n')
            i+=1
        self.contents_.pack(fill='both',expand=1)
        self.discount_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.discount_frame.columnconfigure((0,1),weight=1)
        self.discount_label=customtkinter.CTkLabel(self.discount_frame,text='自訂優惠')
        self.discount_entry=customtkinter.CTkEntry(self.discount_frame)
        self.sum_label=customtkinter.CTkLabel(self.discount_frame,text='總計')
        self.money_label=customtkinter.CTkLabel(self.discount_frame,text='XX元')
        self.sum_label.grid(row=2,column=0,sticky='w')
        self.money_label.grid(row=2,column=1,sticky='e')
        self.discount_label.grid(row=0,column=0,sticky='w')
        self.discount_entry.grid(row=0,column=1)
        self.discount_frame.pack(anchor='s')
        self.confirm_bt=customtkinter.CTkButton(self,text='確定下單',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),width=300)
        self.reset_bt=customtkinter.CTkButton(self,text='重設訂單',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),width=300)
        self.confirm_bt.pack(pady=10)
        self.reset_bt.pack()
class sum_list(customtkinter.CTkFrame):
    def __init__(self, master,a,buy_list,bt_group, **kwargs):
        super().__init__(master, **kwargs)
        self.rowconfigure(len(buy_list),weight=1)
        self.a=a
        self.buy_list=buy_list
        self.bt_group=bt_group
        
        if self.a!='':
            self.buy_list[self.a]=[self.bt_group[self.a][0].get(),self.bt_group[self.a][1]]
            if self.buy_list[self.a][0]==0:del self.buy_list[self.a]
            i=0
            for key,value in self.buy_list.items():
                name_=customtkinter.CTkLabel(self,text=f'{key}',text_color='black')
                number_=customtkinter.CTkLabel(self,text=f'X{value[0]:5}',text_color='black')
                price_=customtkinter.CTkLabel(self,text=f'{value[0]*value[1]}',text_color='black')
                name_.grid(row=i,column=0, padx=20, pady=3,sticky='nw')
                number_.grid(row=i,column=1, padx=20, pady=3,sticky='n')
                price_.grid(row=i,column=2, padx=20, pady=3,sticky='n')
                i+=1
class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("#DDDDDD", "#DDDDDD"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            if value<=0:
                self.entry.insert(0, 0.0)
            else:
                self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        if value<=0:
           self.entry.insert(0, str(0.0))
        else: 
            self.entry.insert(0, str(float(value)))