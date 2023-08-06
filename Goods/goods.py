import tkinter as tk
import customtkinter
from typing import Union
from typing import Callable
from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.crud import *
import pandas as pd
import os
from PIL import Image
# Goods () 品項
class Goods_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bt_frame=button_Frame(self,fg_color=("#EEEEEE"))
        self.bt_frame.pack(pady=40,padx=40,anchor='nw')
        self.goods_F=goods_frame(self,fg_color=("#EEEEEE"))
        self.goods_F.pack(pady=20,padx=40,anchor='nw',fill='both',expand=1)
        
        def input_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.input_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.goods_F.pack_forget()
            self.goods_F=goods_frame(self,  fg_color = ("#EEEEEE"))
            self.goods_F.pack(pady=20,padx=40,anchor='nw',fill='both',expand=1)
        def add_button_click(event):
            self.bt_frame.reset_color()
            self.bt_frame.edit_button.configure(fg_color = ("#5b5a5a"),text_color='white')
            self.goods_F.pack_forget()
            self.goods_F=add_frame(self,  fg_color = ("#EEEEEE"))
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
        self.delete_photo = customtkinter.CTkImage(light_image=Image.open("image\\close.png"),
                                  dark_image=Image.open("image\\close.png"),
                                  size=(30, 30))        
        self.toplevel_window = None
        a=customtkinter.CTkFrame(self,fg_color=("#EEEEEE"))
        search_label=customtkinter.CTkLabel(a,text='品項查詢',fg_color = ("#EEEEEE"),text_color='black')
        # search_label.grid(row=0,column=0,padx=30,pady=5,sticky='ew')
        search_label.pack(side='left')
        self.search=customtkinter.CTkEntry(a,fg_color = ("#EEEEEE"),text_color='black')
        self.search_bt=customtkinter.CTkButton(a, text="Q", width=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'),
                                                        command=self.search_)
        self.search.pack(side='left')
        self.search_bt.pack(side='left')
        bt1=customtkinter.CTkButton(a,text='新增單個品項',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.add_product)
        bt2=customtkinter.CTkButton(a,text='匯出品項資料',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.output_excel)
        bt1.pack(anchor='e',padx=30,pady=5)
        bt2.pack(anchor='e',padx=30,pady=5)
        a.pack(anchor='n',fill='x',padx=30,pady=5)
        self.history_frame=customtkinter.CTkScrollableFrame(self,fg_color = ("#EEEEEE"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='品項名稱',text_color='black')
        order_n1=customtkinter.CTkLabel(self.history_frame,text='內容物',text_color='black')
        order_n2=customtkinter.CTkLabel(self.history_frame,text='重量',text_color='black')
        order_n3=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black')
        order_n4=customtkinter.CTkLabel(self.history_frame,text='刪除',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        
        self.history_frame.pack(fill='both',anchor='n',expand=1,pady=40,padx=30)
        prodcuts=get_all_products(Session(engine))
        l=1
        def gen_cmd(i):return lambda:self.delete(i)
        for i in prodcuts:
            order_n=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Name}',text_color='black')
            order_n1=customtkinter.CTkLabel(self.history_frame,text=f'{"" if i.content==None else i.content}',text_color='black')
            order_n2=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Weight}',text_color='black')
            order_n3=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Price}',text_color='black')
            order_n4=customtkinter.CTkButton(self.history_frame,image=self.delete_photo, fg_color = ("#EEEEEE"),hover=False,text='',text_color='black',command=gen_cmd(i.prodcut_ID))
            order_n.grid(row=l,column=0,sticky='w')
            order_n1.grid(row=l,column=1,sticky='w')
            order_n2.grid(row=l,column=2)
            order_n3.grid(row=l,column=3)
            order_n4.grid(row=l,column=4)
            l+=1
    def search_(self):
        pd=search_pd(db=Session(engine),pd_name=self.search.get())
        self.history_frame.pack_forget()
        self.history_frame=customtkinter.CTkScrollableFrame(self,fg_color = ("#EEEEEE"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='品項名稱',text_color='black')
        order_n1=customtkinter.CTkLabel(self.history_frame,text='內容物',text_color='black')
        order_n2=customtkinter.CTkLabel(self.history_frame,text='重量',text_color='black')
        order_n3=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black')
        order_n4=customtkinter.CTkLabel(self.history_frame,text='刪除',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        self.history_frame.pack(fill='both',anchor='n',expand=1,pady=40,padx=30)
        l=1
        def gen_cmd(i):return lambda:self.delete(i)
        for i in pd:
            order_n=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Name}',text_color='black')
            order_n1=customtkinter.CTkLabel(self.history_frame,text=f'{"" if i.content==None else i.content}',text_color='black')
            order_n2=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Weight}',text_color='black')
            order_n3=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Price}',text_color='black')
            order_n4=customtkinter.CTkButton(self.history_frame,image=self.delete_photo, fg_color = ("#EEEEEE"),hover=False,text='',text_color='black',command=gen_cmd(i.prodcut_ID))
            order_n.grid(row=l,column=0,sticky='w')
            order_n1.grid(row=l,column=1,sticky='w')
            order_n2.grid(row=l,column=2)
            order_n3.grid(row=l,column=3)
            order_n4.grid(row=l,column=4)
            l+=1
    def delete(self,i):
        delete_product(Session(engine),i)
        self.history_frame.pack_forget()
        self.history_frame=customtkinter.CTkScrollableFrame(self,fg_color = ("#EEEEEE"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='品項名稱',text_color='black')
        order_n1=customtkinter.CTkLabel(self.history_frame,text='內容物',text_color='black')
        order_n2=customtkinter.CTkLabel(self.history_frame,text='重量',text_color='black')
        order_n3=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black')
        order_n4=customtkinter.CTkLabel(self.history_frame,text='刪除',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        self.history_frame.pack(fill='both',anchor='n',expand=1,pady=40,padx=30)
        
        i=1
        prodcuts=get_all_products(Session(engine))
        l=1
        def gen_cmd(i):return lambda:self.delete(i)
        for i in prodcuts:
            order_n=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Name}',text_color='black')
            order_n1=customtkinter.CTkLabel(self.history_frame,text=f'{"" if i.content==None else i.content}',text_color='black')
            order_n2=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Weight}',text_color='black')
            order_n3=customtkinter.CTkLabel(self.history_frame,text=f'{i.product_Price}',text_color='black')
            order_n4=customtkinter.CTkButton(self.history_frame,image=self.delete_photo, fg_color = ("#EEEEEE"),hover=False,text='',text_color='black',command=gen_cmd(i.prodcut_ID))
            order_n.grid(row=l,column=0,sticky='w')
            order_n1.grid(row=l,column=1,sticky='w')
            order_n2.grid(row=l,column=2)
            order_n3.grid(row=l,column=3)
            order_n4.grid(row=l,column=4)
            l+=1
        self.history_frame.pack(fill='both',anchor='n',expand=1,pady=40,padx=30)
        
    def add_product(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = add_product_ToplevelWindow(self)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def output_excel(self):
        try:
            query = 'SELECT * FROM product'
            df = pd.read_sql_query(query, engine)
            for index,row in df.iterrows(): 
                if row['content']==None:df.at[index, 'content'] = row['product_Name']
            df.to_excel('output_good.xlsx', index=False)
            current_directory = os.getcwd()
            tk.messagebox.showinfo(title='匯出成功', message=f"匯出成功\n檔案位置：{current_directory}\\output_good.xlsx", )              
        except Exception as e:
            tk.messagebox.showinfo(title='匯出失敗', message=f"匯出失敗{e}", )
class add_product_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('新增單品各項')
        self.geometry("400x200")
        self.columnconfigure((0,1),weight=1)
        name=customtkinter.CTkLabel(self,text='品項名稱：')
        weight=customtkinter.CTkLabel(self,text='重量：')
        price=customtkinter.CTkLabel(self,text='價格：')
        self.name_entry=customtkinter.CTkEntry(self,)
        self.weight_entry=customtkinter.CTkEntry(self,)
        self.price_entry=customtkinter.CTkEntry(self,)
        confirm=customtkinter.CTkButton(self,text='確定新增',command=self.add)
        cancel=customtkinter.CTkButton(self,text='取消',command=self.destroy)
        confirm.grid(row=3,column=1,pady=10)
        cancel.grid(row=3,column=0,pady=10)
        name.grid(row=0,column=0,pady=10)
        weight.grid(row=1,column=0,pady=10)
        price.grid(row=2,column=0,pady=10)
        self.name_entry.grid(row=0,column=1,pady=10)
        self.weight_entry.grid(row=1,column=1,pady=10)
        self.price_entry.grid(row=2,column=1,pady=10)
    def add(self):
        try:
            add_pd(db=Session(engine),p_name=self.name_entry.get(),p_weight=self.weight_entry.get(),p_price=self.price_entry.get())
            self.destroy()
            tk.messagebox.showinfo(title='新增成功', message="新增成功", )  
        except:
            tk.messagebox.showinfo(title='新增失敗', message="新增失敗", )  
class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #5b5a5afg_color = ("#5b5a5a"),text_color='white'
        self.input_button = customtkinter.CTkButton(self, text="品項管理", width=150, height=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='white',border_width=2,corner_radius=0,
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
        self.buy_photo = customtkinter.CTkImage(light_image=Image.open("image\\cart.png"),
                                  dark_image=Image.open("image\\cart.png"),
                                  size=(30, 30))        
        self.product_=customtkinter.CTkFrame(self, fg_color = ("#EEEEEE"))
        prodcuts=get_all_products(Session(engine))
        self.toplevel_window = None
        self.bt_group={}
        self.buy_list={}
        self.a_frame=customtkinter.CTkScrollableFrame(self.product_,fg_color = ("#EEEEEE"))
        for i in range(5):
            self.a_frame.columnconfigure(i,weight=1)
        def gen_cmd(i):return lambda:self.buy_bt_click(i)
        for i in range(len(prodcuts)):
            label_Name=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Name,text_color='black')
            label_Name.grid(row=i,column=0,sticky='w')
            label_Weight=customtkinter.CTkLabel(self.a_frame,text=prodcuts[i].product_Weight,text_color='black')
            label_Weight.grid(row=i,column=1)
            label_price=customtkinter.CTkLabel(self.a_frame,text=f'{prodcuts[i].product_Price}元',text_color='black')
            label_price.grid(row=i,column=2)
            
            spinbox_1 = FloatSpinbox(self.a_frame, width=150, step_size=1)
            self.bt_group[prodcuts[i].product_Name]=[spinbox_1,prodcuts[i].product_Price]
            spinbox_1.grid(row=i,column=4,pady=0)
            buy_button=customtkinter.CTkButton(self.a_frame,image=self.buy_photo, text="",hover=False,  fg_color = ("#EEEEEE"),command=gen_cmd(prodcuts[i].product_Name))
            buy_button.grid(row=i,column=5, padx=30, pady=0)
            
        self.a_frame.pack(side='left',anchor='n',fill='both',expand=1)
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        # self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')        
        # self.product_=product_Frame(self, fg_color = ("#DDDDDD"))
        self.product_.pack(fill='both',expand=1,pady=5)
    def buy_bt_click(self,a):
        name=self.sum_frame_.name_entry.get()
        weight=self.sum_frame_.weight_entry.get()
        price=self.sum_frame_.price_entry.get()
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a=a,buy_list=self.buy_list,bt_group=self.bt_group,name=name,weight=weight,price=price,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        # self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
        self.buy_list=self.sum_frame_.buy_list
        
    def reset_(self):
        self.buy_list={}
        self.sum_frame_.pack_forget()
        self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        self.sum_frame_.reset_bt.configure(command=self.reset_)
        # self.sum_frame_.confirm_bt.configure(command=self.add_od)
        self.sum_frame_.pack(side='right',anchor='n',fill='both')
    def add_od(self):
        print('ok')
        pass
        # add_order(db=Session(engine),phone=self.phone.get(),Pick_up=self.pick_up.get(),remark=self.Remark_textbox.get(1.0,'end'),product_=self.buy_list,m_id='1',date_=self.date_.get_date())
        # self.sum_frame_.pack_forget()
        # self.sum_frame_=sum_Frame(self.product_,a='',buy_list=self.buy_list,bt_group=self.bt_group,  fg_color = ("#EEEEEE"))
        # self.sum_frame_.reset_bt.configure(command=self.reset_)
        # self.sum_frame_.pack(side='right',anchor='n',fill='both')
class sum_Frame(customtkinter.CTkFrame):
    def __init__(self, master,a,buy_list,bt_group,name='',weight='',price='', **kwargs):
        super().__init__(master, **kwargs)
        f=customtkinter.CTkFrame(self,  fg_color = ("#EEEEEE"))
        f.columnconfigure(0,weight=1)
        f.columnconfigure(1,weight=5)
        name_label=customtkinter.CTkLabel(f,text='名稱',text_color='black')
        self.name_entry=customtkinter.CTkEntry(f,fg_color = ("#EEEEEE"),text_color='black')
        weight_label=customtkinter.CTkLabel(f,text='重量',text_color='black')
        self.weight_entry=customtkinter.CTkEntry(f,fg_color = ("#EEEEEE"),text_color='black')
        price_label=customtkinter.CTkLabel(f,text='價錢',text_color='black')
        self.price_entry=customtkinter.CTkEntry(f,fg_color = ("#EEEEEE"),text_color='black')
        name_label.grid(row=0,column=0,sticky='w')
        self.name_entry.grid(row=0,column=1,padx=30,sticky='ew')
        self.name_entry.insert(customtkinter.END,name)
        self.weight_entry.insert(customtkinter.END,weight)
        self.price_entry.insert(customtkinter.END,price)
        weight_label.grid(row=1,column=0,sticky='w')
        self.weight_entry.grid(row=1,column=1,padx=30,sticky='ew')
        price_label.grid(row=2,column=0,sticky='w')
        self.price_entry.grid(row=2,column=1,padx=30,sticky='ew')
        f.pack(anchor='w',fill='x')
        contents_label=customtkinter.CTkLabel(self,text='內容物',text_color='black')
        contents_label.pack(anchor='w')
        self.a=a
        self.buy_list=buy_list
        self.bt_group=bt_group
        self.contents_=customtkinter.CTkFrame(self,  fg_color = ("#EEEEEE"),border_color='black',border_width=1)
        self.contents_.rowconfigure(len(buy_list),weight=1)
        fake_name_=customtkinter.CTkLabel(self.contents_,text=f'西式煙燻火腿(小圓)',text_color=("#EEEEEE"))
        fake_number_=customtkinter.CTkLabel(self.contents_,text=f'X{5.0:5}',text_color=("#EEEEEE"))
        fake_price_=customtkinter.CTkLabel(self.contents_,text=f'{290.5}',text_color=("#EEEEEE"))
        fake_name_.grid(row=0,column=0, padx=20, pady=3,sticky='nw')
        fake_number_.grid(row=0,column=1, padx=20, pady=3,sticky='n')
        fake_price_.grid(row=0,column=2, padx=20, pady=3,sticky='n')
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
        self.confirm_bt=customtkinter.CTkButton(self,text='確定下單',command=lambda: self.add_gift_box_(pd=self.buy_list))
        self.reset_bt=customtkinter.CTkButton(self,text='重設訂單')
        self.confirm_bt.pack(pady=20)
        self.reset_bt.pack()
    def add_gift_box_(self,pd):
        # add_gift_box(db=Session(engine),pd=pd,name=self.name_entry.get(),weight=self.weight_entry.get(),price=self.price_entry.get())
        try:
            add_gift_box(db=Session(engine),pd=pd,name=self.name_entry.get(),weight=self.weight_entry.get(),price=self.price_entry.get())
            tk.messagebox.showinfo(title='新增成功', message="新增成功", )
        except:
            tk.messagebox.showinfo(title='新增失敗', message="新增失敗", )
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
        self.entry.insert(0, "0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            if value<=0:
                self.entry.insert(0, 0)
            else:
                self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        if value<=0:
           self.entry.insert(0, str(0))
        else: 
            self.entry.insert(0, str(int(value)))
        