import customtkinter
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine
from tkcalendar import DateEntry
class finish_search_fame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.toplevel_window = None
        # 搜尋
        search_f=customtkinter.CTkFrame(self,fg_color=("#EEEEEE"))

        self.sell_date_entry = DateEntry(search_f, selectmode='day',
                                                    font=("microsoft yahei", 20),)        
        self.reset_btn = customtkinter.CTkButton(search_f,width=200,height=40,
                                                    fg_color="#3B8ED0",
                                                    text="重設查詢",
                                                    font=("microsoft yahei", 20, 'bold'),
                                                    )        

        self.search=customtkinter.CTkEntry(search_f,fg_color = ("#DDDDDD"),text_color='black',placeholder_text="客戶電話")
        self.search_bt=customtkinter.CTkButton(search_f, text="確認查詢",width=200, height=40,
                                                        fg_color=("#3B8ED0"),
                                                        font=("microsoft yahei", 20, 'bold'),
                                                        command=self.search_A)
        self.search.pack(side='top',pady=40,padx=30,fill='x')
        self.sell_date_entry.pack(side='top',pady=40,padx=30)
        self.reset_btn.pack(side='bottom',pady=20,padx=30)        
        self.search_bt.pack(side='bottom',pady=20,padx=30)
        search_f.pack(anchor='n',fill='both',side='left',padx=30,pady=5)

        # 客戶資訊
        top=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        top.columnconfigure((0,1),weight=1)
        self.customer_name = customtkinter.CTkLabel(top,text="客戶名稱：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.address = customtkinter.CTkLabel(top,text="地址：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.phone = customtkinter.CTkLabel(top,text="　　手機：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.remark = customtkinter.CTkLabel(top,text="備註：", font=("microsoft yahei", 20, 'bold'),text_color='black')
        self.customer_name.grid(row=0,column=0,sticky='w')
        self.address.grid(row=0,column=1,sticky='w')
        self.phone.grid(row=1,column=0,sticky='w')
        self.remark.grid(row=1,column=1,sticky='w')
        top.pack(fill='x')

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
        
        self.history_frame.pack(fill='both',anchor='n',pady=40,padx=30)
    def search_A(self):
        try:
            self.od_l={}
            user=get_user(Session(engine),user_phone=self.search.get())
            self.customer_name.configure(text=f'客戶名稱：{user.Name}')
            self.address.configure(text=f'地址：：{user.Address}')
            self.phone.configure(text=f'　　手機：：{user.Phone}')
            self.remark.configure(text=f'備註：{user.Remark}')
            
            for i in user.orders:
                if i.order_number in self.od_l:
                    self.od_l[i.order_number][1]+=f',{i.p_ID_.product_Name}'
                else:
                    self.od_l[i.order_number]=[i.M_ID_.ID,i.p_ID_.product_Name,i.money,i.collect_money]
        except:
            self.od_l={}        
        self.history_frame.pack_forget()
        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#DDDDDD"))
        self.history_frame.columnconfigure((0,2,3,4,5),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='廠商資訊',text_color='black')
        order_n1=customtkinter.CTkLabel(self.history_frame,text='訂單內容',text_color='black')
        order_n2=customtkinter.CTkLabel(self.history_frame,text='價錢',text_color='black')
        order_n3=customtkinter.CTkLabel(self.history_frame,text='已收金額',text_color='black')
        order_n4=customtkinter.CTkLabel(self.history_frame,text='餘額',text_color='black')
        order_n5=customtkinter.CTkLabel(self.history_frame,text='',text_color='black')
        order_n.grid(row=0,column=0,sticky='w')
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        order_n5.grid(row=0,column=5)
        self.history_frame.pack(fill='x',anchor='n',pady=40,padx=30)
        l=1
        def gen_cmd(i,l):return lambda:self.update_(i,l)
        for key,value in self.od_l.items():
            order_n=customtkinter.CTkLabel(self.history_frame,text=f'{value[0]}',text_color='black')
            order_n1=customtkinter.CTkLabel(self.history_frame,text=f'{value[1]}',text_color='black')
            order_n2=customtkinter.CTkLabel(self.history_frame,text=f'{value[2]}',text_color='black')
            order_n3=customtkinter.CTkLabel(self.history_frame,text=f'{value[3]}',text_color='black')
            order_n4=customtkinter.CTkLabel(self.history_frame,text=f'{value[2]-value[3]}',text_color='black')
            order_n5=customtkinter.CTkButton(self.history_frame,text='確認入賬',text_color='black',command=gen_cmd(key,value[0]))
            order_n.grid(row=l,column=0,sticky='w')
            order_n1.grid(row=l,column=1,sticky='w')
            order_n2.grid(row=l,column=2)
            order_n3.grid(row=l,column=3)
            order_n4.grid(row=l,column=4)
            order_n5.grid(row=l,column=5)
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