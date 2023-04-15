#-*- coding: utf-8 -*-
import tkinter as tk
import customtkinter
from tkcalendar import DateEntry
import customtkinter as ctk
from typing import Union
from typing import Callable
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine
# Order () 訂單
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
            self.input_order_.search.search_bt.configure(command=bt)
            self.input_order_.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        self.bt_frame.input_button.bind("<Button-1>", input_button_click)
        self.bt_frame.edit_button.bind("<Button-1>", edit_button_click)
        self.bt_frame.finish_button.bind("<Button-1>", finish_button_click)
        def bt():
            print('s')
class edit_order(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        edit_top_=edit_top(self,fg_color = ("#DDDDDD"))
        edit_top_.pack(fill='x',padx=30,pady=5)
        ol=order_List(self,fg_color = ("#DDDDDD"))
        ol.pack(fill='x',padx=30,pady=5)
class edit_top(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        for i in range(7):
            self.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self, text="電話",text_color='black')
        self.phone=customtkinter.CTkEntry(self, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black')
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self, text="通路",text_color='black')
        self.path=customtkinter.CTkComboBox(self,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self, text="取貨方式",text_color='black')
        self.pick_up=customtkinter.CTkComboBox(self,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self, text="日期",text_color='black')
        self.date_=DateEntry(self,selectmode='day')
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.date_1=DateEntry(self,selectmode='day')
        self.date_1.grid(row=1,column=3,padx=30,pady=5)
        self.money_label=customtkinter.CTkLabel(self, text="金額",text_color='black')
        self.money=customtkinter.CTkEntry(self, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black')
        self.money2=customtkinter.CTkEntry(self, placeholder_text="",fg_color = ("#DDDDDD"),text_color='black')
        self.money_label.grid(row=0,column=4,padx=30,pady=5)
        self.money.grid(row=0,column=5,padx=30,pady=5)
        self.money2.grid(row=1,column=5,padx=30,pady=5)
        reset_bt=customtkinter.CTkButton(self,text='重新設定', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        )
        reset_bt.grid(row=0,column=6,padx=30,pady=5)
        search=customtkinter.CTkButton(self,text='確定查詢', width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        )
        search.grid(row=1,column=6,padx=30,pady=5)
class finish_frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.search=finish_search_fame(self,fg_color = ("#DDDDDD"))
        self.search.pack(fill='both',side='left',expand=1,padx=15,pady=5)
        search1=finish_frame2(self,fg_color = ("#DDDDDD"))
        search1.pack(fill='both',side='left',expand=1,padx=15,pady=5)
class finish_frame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0,weight=1)
        self.order_number=customtkinter.CTkLabel(self,text='訂單編號',fg_color = ("#DDDDDD"),text_color='black')
        self.order_number.grid(row=0,column=0,sticky='w')
        self.order_item=customtkinter.CTkLabel(self,text='訂單品項',fg_color = ("#DDDDDD"),text_color='black')
        self.order_item.grid(row=1,column=0,sticky='w')
        self.p_1=customtkinter.CTkScrollableFrame(self)
        self.p_1.grid(row=2,column=0,sticky='ew')
        self.bt_group=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.up_bt=customtkinter.CTkButton(self.bt_group,text='up', width=40,corner_radius=0)
        self.reset_bt=customtkinter.CTkButton(self.bt_group,text='re', width=40,corner_radius=0)
        self.down_bt=customtkinter.CTkButton(self.bt_group,text='do', width=40,corner_radius=0)
        self.up_bt.grid(row=3,column=0,padx=5,pady=5)
        self.reset_bt.grid(row=3,column=1,padx=5,pady=5)
        self.down_bt.grid(row=3,column=2,padx=5,pady=5)
        self.bt_group.grid(row=3)
        self.p_2=customtkinter.CTkScrollableFrame(self)
        self.p_2.grid(row=4,column=0,sticky='ew')
        self.down_bt_group=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.down_bt_group.columnconfigure((0,1),weight=1)
        self.edit_bt=customtkinter.CTkButton(self.down_bt_group,text='編輯訂單', width=40,corner_radius=0)
        self.cancel_bt=customtkinter.CTkButton(self.down_bt_group,text='取消訂單', width=40,corner_radius=0)
        self.partially_completed_bt=customtkinter.CTkButton(self.down_bt_group,text='完成部分訂單', width=40,corner_radius=0)
        self.finish_bt=customtkinter.CTkButton(self.down_bt_group,text='完成訂單', width=40,corner_radius=0)
        self.edit_bt.grid(row=0,column=0,padx=5,pady=5,sticky='ew')
        self.cancel_bt.grid(row=0,column=1,padx=5,pady=5,sticky='ew')
        self.partially_completed_bt.grid(row=1,column=0,padx=5,pady=5,sticky='ew')
        self.finish_bt.grid(row=1,column=1,padx=5,pady=5,sticky='ew')
        self.down_bt_group.grid(row=5,column=0,sticky='ew')          
class finish_search_fame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)
        search_label=customtkinter.CTkLabel(self,text='訂單編號查詢',fg_color = ("#DDDDDD"),text_color='black')
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky='ew')
        search=customtkinter.CTkEntry(self,fg_color = ("#DDDDDD"),text_color='black')
        self.search_bt=customtkinter.CTkButton(self, text="Q", width=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'))
        self.search_bt.grid(row=0,column=2,sticky='ew')
        search.grid(row=0,column=1,sticky='ew',pady=5)
        f_order_list=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        for i in range(3):
            f_order_list.columnconfigure(i,weight=1)
        
        a=customtkinter.CTkLabel(f_order_list,text='訂單編號',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=0)
        a1=customtkinter.CTkLabel(f_order_list,text='取貨日期',fg_color = ("#DDDDDD"),text_color='black')
        a1.grid(row=0,column=1)
        a2=customtkinter.CTkLabel(f_order_list,text='取貨方式',fg_color = ("#DDDDDD"),text_color='black')
        a2.grid(row=0,column=2) 
        a3=customtkinter.CTkLabel(f_order_list,text='是否取貨',fg_color = ("#DDDDDD"),text_color='black')
        a3.grid(row=0,column=3)   
        f_order_list.grid(row=3,column=0,columnspan=2,sticky='ew',pady=30)              
class order_List(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        for i in range(9):
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
        a=customtkinter.CTkLabel(self,text='編輯',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=7)
        a=customtkinter.CTkLabel(self,text='刪除',fg_color = ("#DDDDDD"),text_color='black')
        a.grid(row=0,column=8)           
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
        self.columnconfigure((0,1),weight=1)
        self.input_top_=input_top(self, fg_color = ("#DDDDDD"))
        self.input_top_.pack(fill='x',padx=30,pady=5)
        self.product_=product_Frame(self, fg_color = ("#DDDDDD"))
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
# https://gist.github.com/apua/e43f007fbc9813ae97f7831ed25bb62b
class input_top(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        for i in range(6):
            self.columnconfigure(i,weight=1)
        self.ph_label=customtkinter.CTkLabel(self, text="電話",text_color='black')
        self.phone=customtkinter.CTkEntry(self, placeholder_text="電話",fg_color = ("#DDDDDD"),text_color='black')
        self.ph_label.grid(row=0,column=0,padx=30,pady=5)
        self.phone.grid(row=0, column=1,padx=30,pady=5)
        self.path_label=customtkinter.CTkLabel(self, text="通路",text_color='black')
        self.path=customtkinter.CTkComboBox(self,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.path_label.grid(row=1,column=0,padx=30,pady=5)
        self.path.grid(row=1,column=1,padx=30,pady=5)
        self.pick_up_label=customtkinter.CTkLabel(self, text="取貨方式",text_color='black')
        self.pick_up=customtkinter.CTkComboBox(self,values=["option 1", "option 2"],fg_color = ("#DDDDDD"),text_color='black')
        self.pick_up_label.grid(row=2,column=0,padx=30,pady=5)
        self.pick_up.grid(row=2,column=1,padx=30,pady=5)
        self.date_label=customtkinter.CTkLabel(self, text="日期",text_color='black')
        self.date_=DateEntry(self,selectmode='day')
        self.date_label.grid(row=0,column=2,padx=30,pady=5)
        self.date_.grid(row=0,column=3,padx=30,pady=5)
        self.date_1=DateEntry(self,selectmode='day')
        self.date_1.grid(row=1,column=3,padx=30,pady=5)
        self.Remark_label=customtkinter.CTkLabel(self, text="備註",text_color='black')
        self.Remark_label.grid(row=0,column=4,padx=30,pady=5)
        self.Remark_textbox = customtkinter.CTkTextbox(self, corner_radius=0,width=300,fg_color='white',border_color='black',text_color='black',border_width=1)
        self.Remark_textbox.grid(row=0, column=5,rowspan=3,padx=30,pady=5)        
class product_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        prodcuts=get_all_products(Session(engine))
        list1=[['a','小','a元'],['b','大','b元'],['c','小','c元'],['d','小','d元'],['e','小','e元']]
        self.bt_group={}
        self.buy_list={}
        self.a_frame=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
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
            buy_button=customtkinter.CTkButton(self.a_frame, text="buy",command=gen_cmd(prodcuts[i].product_Name))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
            
        self.a_frame.pack(side='left',anchor='n',fill='x',expand=1)
        self.sum_frame_=sum_Frame(self,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
        
    def buy_bt_click(self,a):
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self,a=a,buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
    def reset_(self):
        print('a')
        self.buy_list={}
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
class sum_Frame(customtkinter.CTkFrame):
    def __init__(self, master,a,buy_list,bt_group, **kwargs):
        super().__init__(master, **kwargs)
        self.a=a
        self.buy_list=buy_list
        self.bt_group=bt_group
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
        self.confirm_bt=customtkinter.CTkButton(self,text='確定下單',width=300)
        self.reset_bt=customtkinter.CTkButton(self,text='重設訂單',width=300)
        self.confirm_bt.pack(pady=10)
        self.reset_bt.pack()
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