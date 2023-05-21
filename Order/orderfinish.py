import customtkinter
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine
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