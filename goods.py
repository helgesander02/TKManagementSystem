import tkinter as tk
import customtkinter
from typing import Union
from typing import Callable
from sqlalchemy.orm import Session
from sql_app.database import engine

# Goods () 品項
class Goods_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bt_frame=button_Frame(self,fg_color=("#EEEEEE"))
        self.bt_frame.pack(pady=40,padx=40,anchor='nw')
        self.goods_F=goods_frame(self,fg_color=("#EEEEEE"))
        self.goods_F.pack(pady=20,padx=40,anchor='nw',fill='x')
        
        def input_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.goods_F.pack_forget()
            self.goods_F=goods_frame(self,  fg_color = ("#EEEEEE") ,width=1200 ,height=680)
            self.goods_F.pack(fill='x',pady=20,padx=30,anchor='nw')
        def add_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.edit_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.goods_F.pack_forget()
            self.goods_F=add_frame(self,  fg_color = ("#EEEEEE") ,width=1200 ,height=680)
            self.goods_F.pack(fill='both',expand=1,pady=20,padx=30,anchor='nw')
        self.bt_frame.input_button.bind("<Button-1>", input_button_click)
        self.bt_frame.edit_button.bind("<Button-1>", add_button_click)
class add_frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.product_=product_Frame(self, fg_color = ("#EEEEEE"))
        self.product_.pack(fill='both',expand=1,padx=30,pady=5)
class goods_frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        a=customtkinter.CTkFrame(self,fg_color=("#EEEEEE"))
        search_label=customtkinter.CTkLabel(a,text='訂單編號查詢',fg_color = ("#EEEEEE"),text_color='black')
        # search_label.grid(row=0,column=0,padx=30,pady=5,sticky='ew')
        search_label.pack(side='left')
        search=customtkinter.CTkEntry(a,fg_color = ("#EEEEEE"),text_color='black')
        self.search_bt=customtkinter.CTkButton(a, text="Q", width=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'))
        search.pack(side='left')
        self.search_bt.pack(side='left')
        bt1=customtkinter.CTkButton(a,text='新增單個品項')
        bt2=customtkinter.CTkButton(a,text='匯出品項資料')
        bt1.pack(anchor='e',padx=30,pady=5)
        bt2.pack(anchor='e',padx=30,pady=5)
        a.pack(anchor='n',fill='x',padx=30,pady=5)

        history_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        history_frame.columnconfigure((0,2,3,4),weight=1)
        history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(history_frame,text='品項名稱',text_color='black')
        order_n1=customtkinter.CTkLabel(history_frame,text='內容物',text_color='black')
        order_n2=customtkinter.CTkLabel(history_frame,text='重量',text_color='black')
        order_n3=customtkinter.CTkLabel(history_frame,text='價錢',text_color='black')
        order_n4=customtkinter.CTkLabel(history_frame,text='刪除',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        history_frame.pack(fill='x',anchor='n',pady=40,padx=30)
class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #5b5a5a
        self.input_button = customtkinter.CTkButton(self, text="品項管理", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.input_button.grid(row=0, column=5,padx=30)
        self.edit_button = customtkinter.CTkButton(self, text="新增禮盒", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.edit_button.grid(row=0, column=6,padx=30)


    def reset_color(self):
        self.input_button.configure(fg_color = ("#EEEEEE"),text_color='black')
        self.edit_button.configure(fg_color = ("#EEEEEE"),text_color='black')
class product_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        list1=[['a','小','a元'],['b','大','b元'],['c','小','c元'],['d','小','d元'],['e','小','e元']]
        self.bt_group={}
        self.buy_list={}
        self.a_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        for i in range(len(list1)):
            self.a_frame.columnconfigure(i,weight=1)
        def gen_cmd(i):return lambda:self.buy_bt_click(i)
        for i in range(len(list1)):
            for l in range(len(list1[0])):
                label_=customtkinter.CTkLabel(self.a_frame,text=list1[i][l],text_color='black')
                label_.grid(row=i,column=l,padx=30)
            spinbox_1 = FloatSpinbox(self.a_frame, width=150, step_size=1)
            self.bt_group[list1[i][0]]=spinbox_1
            spinbox_1.grid(row=i,column=4,pady=30)
            buy_button=customtkinter.CTkButton(self.a_frame, text="buy",command=gen_cmd(list1[i][0]))
            buy_button.grid(row=i,column=5, padx=30, pady=3)
        self.a_frame.pack(side='left',anchor='n',fill='x',expand=1)
        self.sum_frame_=sum_Frame(self,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.pack(side='right',anchor='n',fill='y')
    def buy_bt_click(self,a):
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self,a=a,buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.pack(side='right',anchor='n',fill='y')
class sum_Frame(customtkinter.CTkFrame):
    def __init__(self, master,a,buy_list,bt_group, **kwargs):
        super().__init__(master, **kwargs)
        f=customtkinter.CTkFrame(self,  fg_color = ("#EEEEEE"))
        f.columnconfigure((0,1),weight=1)
        name_label=customtkinter.CTkLabel(f,text='名稱',text_color='black')
        name_entry=customtkinter.CTkEntry(f,fg_color = ("#DDDDDD"),text_color='black')
        weight_label=customtkinter.CTkLabel(f,text='重量',text_color='black')
        weight_entry=customtkinter.CTkEntry(f,fg_color = ("#DDDDDD"),text_color='black')
        price_label=customtkinter.CTkLabel(f,text='價錢',text_color='black')
        price_entry=customtkinter.CTkEntry(f,fg_color = ("#DDDDDD"),text_color='black')
        name_label.grid(row=0,column=0,sticky='w')
        name_entry.grid(row=0,column=1,padx=30)
        weight_label.grid(row=1,column=0,sticky='w')
        weight_entry.grid(row=1,column=1,padx=30)
        price_label.grid(row=2,column=0,sticky='w')
        price_entry.grid(row=2,column=1,padx=30)
        f.pack(anchor='w')
        contents_label=customtkinter.CTkLabel(self,text='內容物',text_color='black')
        contents_label.pack(anchor='w')
        self.a=a
        self.buy_list=buy_list
        self.bt_group=bt_group
        self.contents_=customtkinter.CTkFrame(self,  fg_color = ("#EEEEEE"),border_color='black',border_width=1)
        self.contents_.rowconfigure(len(buy_list),weight=1)
        if self.a!='':
            self.buy_list[self.a]=self.bt_group[self.a].get()
            if self.buy_list[self.a]==0:del self.buy_list[self.a]
            i=0
            for key,value in self.buy_list.items():
                la=customtkinter.CTkLabel(self.contents_,text=f'{key}  X{value:7}',text_color='black')
                la.grid(row=i,column=0,columnspan=2, padx=20, pady=3,sticky='n')
                i+=1
        self.contents_.pack(fill='both',expand=1)
        self.confirm_bt=customtkinter.CTkButton(self,text='確定下單')
        self.reset_bt=customtkinter.CTkButton(self,text='重設訂單')
        self.confirm_bt.pack(pady=20)
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
        