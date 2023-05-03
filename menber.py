import tkinter as tk
import customtkinter
from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.crud import get_user,save_change,add_data

from tkinter import *
# Menber () 會員
class Menber_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id=''
        self.columnconfigure((0,1,2,3),weight=1)
        search_=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        search_.columnconfigure((1),weight=1)
        search_label=customtkinter.CTkLabel(search_,text='會員查詢',fg_color = ("#EEEEEE"),text_color='black')
        search_label.grid(row=0,column=0,padx=30,pady=5,sticky='ew')
        self.search=customtkinter.CTkEntry(search_,fg_color = ("#EEEEEE"),text_color='black')
        self.search_bt=customtkinter.CTkButton(search_, text="Q", width=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'),
                                                        command=self.member_search_click)
        self.search_bt.grid(row=0,column=3,sticky='ew')
        self.search.grid(row=0,column=1,sticky='ew')

        search_.grid(row=0,column=0,pady=30,padx=30,sticky='w')

        bt_group=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        # bt_group.columnconfigure((0,1,2),weight=1)
        confirm_bt=customtkinter.CTkButton(bt_group,text='確認')
        edit_bt=customtkinter.CTkButton(bt_group,text='編輯',command=self.open_edit_toplevel)
        add_bt=customtkinter.CTkButton(bt_group,text='新增',command=self.open_add_toplevel)
        confirm_bt.grid(row=0,column=0,padx=10)
        edit_bt.grid(row=0,column=1,padx=10)
        add_bt.grid(row=0,column=2,padx=10)

        bt_group.grid(row=1,column=0,padx=30,sticky='w')

        member_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.member_label=customtkinter.CTkLabel(member_frame,text='會員編號',text_color='black')
        self.member_name=customtkinter.CTkLabel(member_frame,text='名稱',text_color='black')
        self.member_address=customtkinter.CTkLabel(member_frame,text='地址',text_color='black')
        self.member_label.grid(row=0,column=0,sticky='w')
        self.member_name.grid(row=1,column=0,sticky='w')      
        self.member_address.grid(row=2,column=0,sticky='w')

        member_frame.grid(row=0,column=1,rowspan=2,sticky='w')

        history_label=customtkinter.CTkLabel(self,text='歷史紀錄',text_color='black')
        history_label.grid(row=3,column=0,sticky='w',padx=30,pady=50)
        history_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        history_frame.columnconfigure((0,2,3,4),weight=1)
        history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(history_frame,text='訂單編號',text_color='black')
        order_n1=customtkinter.CTkLabel(history_frame,text='訂單項目',text_color='black')
        order_n2=customtkinter.CTkLabel(history_frame,text='金額',text_color='black')
        order_n3=customtkinter.CTkLabel(history_frame,text='編輯',text_color='black')
        order_n4=customtkinter.CTkLabel(history_frame,text='刪除',text_color='black')
        order_n.grid(row=0,column=0)
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        history_frame.grid(row=4,column=0,columnspan=5,sticky='ew')
        self.toplevel_window = None
        
    def button_click(self):
        print("button click")
    def member_search_click(self):
        user=get_user(Session(engine),self.search.get())
        try:
            self.user_id=user.Phone
            self.member_label.configure(text=f'會員編號：{user.ID}')
            self.member_name.configure(text=f'名稱：{user.Name}')
            self.member_address.configure(text=f'地址：{user.Address}')
        except:
            self.member_label.configure(text=f'會員編號：無結果')
            self.member_name.configure(text=f'名稱：無結果')
            self.member_address.configure(text=f'地址：無結果')
    def open_edit_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = edit_ToplevelWindow(self,user_id=self.user_id)
        else:
            self.toplevel_window.focus()  
    def open_add_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = add_ToplevelWindow(self)        
        else:
            self.toplevel_window.focus()
          
class edit_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,user_id:str, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x500")
        try:
            self.user_id=user_id
            self.columnconfigure((0,1),weight=1)
            self.rowconfigure((2,3),weight=2)
            user=get_user(Session(engine),self.user_id)
            edit_n=customtkinter.CTkLabel(self,text='姓名',text_color='black')
            edit_n1=customtkinter.CTkLabel(self,text='電話',text_color='black')
            edit_n2=customtkinter.CTkLabel(self,text='地址',text_color='black')
            edit_n3=customtkinter.CTkLabel(self,text='備註',text_color='black')
            self.edit_entry_n=customtkinter.CTkEntry(self)
            self.edit_entry_n1=customtkinter.CTkEntry(self)
            self.edit_entry_n2=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            self.edit_entry_n3=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            
            self.edit_entry_n.insert(END,f'{user.Name}')
            self.edit_entry_n1.insert(END,f'{user.Phone}')
            self.edit_entry_n2.insert(END,f'{user.Address}')
            self.edit_entry_n3.insert(END,f'{user.Remark}')
            self.cancel_bt=customtkinter.CTkButton(self,text='取消',command=self.cancel_click)
            confirm_bt=customtkinter.CTkButton(self,text='確定更改',command=self.confirm_edit)
            self.cancel_bt.grid(row=4,column=0,sticky='e',padx=30,pady=10)
            confirm_bt.grid(row=4,column=1,sticky='e',padx=30,pady=10)

            edit_n.grid(row=0,column=0)
            edit_n1.grid(row=1,column=0)
            edit_n2.grid(row=2,column=0)
            edit_n3.grid(row=3,column=0)
            self.edit_entry_n.grid(row=0,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n1.grid(row=1,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n2.grid(row=2,column=1,sticky='nsew',padx=10,pady=10)
            self.edit_entry_n3.grid(row=3,column=1,sticky='nsew',padx=10,pady=10)
        except:
            error_label=customtkinter.CTkLabel(self,text='查詢失敗，請回上層進行查詢')
            error_bt=customtkinter.CTkButton(self,text='回上層',command=self.cancel_click)
            error_label.pack(anchor='center',fill='y',pady=30)
            error_bt.pack(anchor='center',fill='y',pady=10)
    def cancel_click(self):
        self.destroy()
    def confirm_edit(self):
        save_change(Session(engine),name=self.edit_entry_n.get(),phone=self.edit_entry_n1.get(),address=self.edit_entry_n2.get(1.0,END),remark=self.edit_entry_n3.get(1.0,END),user_id=self.user_id)
        self.destroy()
class add_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x500")
        
        try:
            self.columnconfigure((0,1),weight=1)
            self.rowconfigure((3,4),weight=2)
            
            edit_n=customtkinter.CTkLabel(self,text='姓名',text_color='black')
            edit_n1=customtkinter.CTkLabel(self,text='電話',text_color='black')
            edit_n2=customtkinter.CTkLabel(self,text='地址',text_color='black')
            edit_n3=customtkinter.CTkLabel(self,text='備註',text_color='black')
            # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
            self.edit_entry_n=customtkinter.CTkEntry(self)
            self.edit_entry_n1=customtkinter.CTkEntry(self)
            self.edit_entry_n2=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            self.edit_entry_n3=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            self.edit_entry_n4=customtkinter.CTkEntry(self)
            
            self.cancel_bt=customtkinter.CTkButton(self,text='取消',command=self.cancel_click)
            confirm_bt=customtkinter.CTkButton(self,text='確定更改',command=self.confirm_edit)
            self.cancel_bt.grid(row=5,column=0,sticky='e',padx=30,pady=10)
            confirm_bt.grid(row=5,column=1,sticky='e',padx=30,pady=10)
            # edit_n4.grid(row=0,column=0)
            edit_n.grid(row=1,column=0)
            edit_n1.grid(row=2,column=0)
            edit_n2.grid(row=3,column=0)
            edit_n3.grid(row=4,column=0)
            self.edit_entry_n.grid(row=1,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n1.grid(row=2,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n2.grid(row=3,column=1,sticky='nsew',padx=10,pady=10)
            self.edit_entry_n3.grid(row=4,column=1,sticky='nsew',padx=10,pady=10)
            self.edit_entry_n4.grid(row=0,column=1,sticky='nsew',padx=10,pady=10)
        except:
            error_label=customtkinter.CTkLabel(self,text='查詢失敗，請回上層進行查詢')
            error_bt=customtkinter.CTkButton(self,text='回上層',command=self.cancel_click)
            error_label.pack(anchor='center',fill='y',pady=30)
            error_bt.pack(anchor='center',fill='y',pady=10)
    def cancel_click(self):
        self.destroy()
    def confirm_edit(self):
        add_data(Session(engine),name=self.edit_entry_n.get(),phone=self.edit_entry_n1.get(),address=self.edit_entry_n2.get(1.0,END),remark=self.edit_entry_n3.get(1.0,END),user_id=self.edit_entry_n4.get())
        self.destroy()


        