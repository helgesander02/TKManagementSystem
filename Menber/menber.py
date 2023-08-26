import tkinter as tk
import customtkinter
from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.crud import get_user,save_change,add_data
from sql_app.crud import *
from tkinter import *
from Order.order import edit_ToplevelWindow as edit_ToplevelWindow_
from PIL import Image
# Menber () 會員
class Menber_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.edit_photo = customtkinter.CTkImage(light_image=Image.open("image\\pencil.png"),
                                  dark_image=Image.open("image\\pencil.png"),
                                  size=(30, 30))
        self.delete_photo = customtkinter.CTkImage(light_image=Image.open("image\\close.png"),
                                  dark_image=Image.open("image\\close.png"),
                                  size=(30, 30))         
        self.user_id=''
        self.columnconfigure((0,1,2,3),weight=1)
        search_=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        search_.columnconfigure((1),weight=1)
        search_label=customtkinter.CTkLabel(search_,text='會員查詢',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        search_label.grid(row=0,column=0,padx=30,pady=5,sticky='ew')
        self.search=customtkinter.CTkEntry(search_,fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.search_bt=customtkinter.CTkButton(search_, text="Q", width=40,
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 14, 'bold'),
                                                        command=self.member_search_click)
        self.search_bt.grid(row=0,column=3,sticky='ew')
        self.search.grid(row=0,column=1,sticky='ew')

        search_.grid(row=0,column=0,pady=30,padx=30,sticky='w')

        bt_group=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        
        edit_bt=customtkinter.CTkButton(bt_group,text='編輯',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.open_edit_toplevel)
        add_bt=customtkinter.CTkButton(bt_group,text='新增',
                                                        fg_color=("#5b5a5a"),
                                                        font=("microsoft yahei", 18, 'bold'),command=self.open_add_toplevel)
        
        edit_bt.grid(row=0,column=1,padx=10)
        add_bt.grid(row=0,column=2,padx=10)

        bt_group.grid(row=1,column=0,padx=30,sticky='w')

        member_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.member_label=customtkinter.CTkLabel(member_frame,text='會員編號',text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.member_name=customtkinter.CTkLabel(member_frame,text='名稱',text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.member_address=customtkinter.CTkLabel(member_frame,text='地址',text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.member_label.grid(row=0,column=0,sticky='w')
        self.member_name.grid(row=1,column=0,sticky='w')      
        self.member_address.grid(row=2,column=0,sticky='w')

        member_frame.grid(row=0,column=1,rowspan=2,sticky='w')

        self.history_label=customtkinter.CTkLabel(self,text='歷史紀錄',text_color='black',font=("microsoft yahei", 18, 'bold'))
        self.history_label.grid(row=3,column=0,sticky='w',padx=30,pady=50)
        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='訂單編號',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n1=customtkinter.CTkLabel(self.history_frame,text='訂單項目',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n2=customtkinter.CTkLabel(self.history_frame,text='金額',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n3=customtkinter.CTkLabel(self.history_frame,text='編輯',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n4=customtkinter.CTkLabel(self.history_frame,text='刪除',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n.grid(row=0,column=0)
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        self.history_frame.grid(row=4,column=0,columnspan=5,sticky='ew')
        self.toplevel_window = None
        self.od_l={}
    def member_search_click(self):
        self.history_frame.grid_forget()
        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.history_frame.columnconfigure((0,2,3,4),weight=1)
        self.history_frame.columnconfigure(1,weight=3)
        order_n=customtkinter.CTkLabel(self.history_frame,text='訂單編號',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n1=customtkinter.CTkLabel(self.history_frame,text='訂單項目',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n2=customtkinter.CTkLabel(self.history_frame,text='金額',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n3=customtkinter.CTkLabel(self.history_frame,text='編輯',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n4=customtkinter.CTkLabel(self.history_frame,text='刪除',text_color='black',font=("microsoft yahei", 18, 'bold'))
        order_n.grid(row=0,column=0)
        order_n1.grid(row=0,column=1,sticky='w')
        order_n2.grid(row=0,column=2)
        order_n3.grid(row=0,column=3)
        order_n4.grid(row=0,column=4)
        self.history_frame.grid(row=4,column=0,columnspan=5,sticky='ew')        
        user=get_user(Session(engine),self.search.get())
        try:
            self.od_l={}
            for i in user.orders:
                if i.order_number in self.od_l:
                    self.od_l[i.order_number][1]+=f',{i.p_ID_.product_Name}'
                else:
                    self.od_l[i.order_number]=[i.order_number,i.p_ID_.product_Name,i.money,user.Phone,i.M_ID]
        except:
            self.od_l={}
        self.od_l=dict(sorted(self.od_l.items(),key=lambda x:x[0]))
        def gen_cmd1(i,l):return lambda:self.edit_(i,l)
        def gen_cmd(i,l):return lambda:self.delete(i,l)
        i=1
        for key,value in self.od_l.items():
            a=customtkinter.CTkLabel(self.history_frame,text=f'{value[0]}',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=0)
            a=customtkinter.CTkLabel(self.history_frame,text=f'{value[1]}',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=1)
            a=customtkinter.CTkLabel(self.history_frame,text=f'{value[2]}',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=2) 
            a=customtkinter.CTkButton(self.history_frame,image=self.edit_photo,hover=False,text='',fg_color = ("#EEEEEE"),text_color='black',command=gen_cmd1(key,value[3]))
            a.grid(row=i,column=3)
            a=customtkinter.CTkButton(self.history_frame,image=self.delete_photo,hover=False,text='',fg_color = ("#EEEEEE"),text_color='black',command=gen_cmd(key,value[-1]))
            a.grid(row=i,column=4)
            i+=1
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
            self.toplevel_window.attributes('-topmost','true')
        else:
            self.toplevel_window.focus()  
    def open_add_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = add_ToplevelWindow(self)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def edit_(self,i,l):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = edit_ToplevelWindow_(self,key=i,M_Name=l)   
            self.toplevel_window.attributes('-topmost','true')   
        else:
            self.toplevel_window.focus()
    def delete(self,i,l):
        delete_od(Session(engine),i,l)
        del self.od_l[i]
        self.history_frame.grid_forget()
        self.history_frame=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        for i in range(9):
            self.history_frame.columnconfigure(i,weight=1)
        self.history_frame.columnconfigure(4,weight=2)
        a=customtkinter.CTkLabel(self.history_frame,text='訂單編號',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=1)
        a=customtkinter.CTkLabel(self.history_frame,text='訂單項目',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=4)
        a=customtkinter.CTkLabel(self.history_frame,text='金額',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=6)
        a=customtkinter.CTkLabel(self.history_frame,text='編輯',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=7)
        a=customtkinter.CTkLabel(self.history_frame,text='刪除',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
        a.grid(row=0,column=8)
        
        i=1
        def gen_cmd1(i,l):return lambda:self.edit_(i,l)
        def gen_cmd(i):return lambda:self.delete(i)
        for key,value in self.od_l.items():
            a=customtkinter.CTkLabel(self.history_frame,text=f'{value[0]}',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=0)
            a=customtkinter.CTkLabel(self.history_frame,text=f'{value[1]}',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=1)
            a=customtkinter.CTkLabel(self.history_frame,text=f'{value[2]}',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=2) 
            a=customtkinter.CTkLabel(self.history_frame,text=f'{value[3]}',fg_color = ("#EEEEEE"),text_color='black',font=("microsoft yahei", 18, 'bold'))
            a.grid(row=i,column=3) 
            a=customtkinter.CTkButton(self.history_frame,image=self.edit_photo,hover=False,text='',fg_color = ("#EEEEEE"),text_color='black',command=gen_cmd1(key,value[3]))
            a.grid(row=i,column=7)
            a=customtkinter.CTkButton(self.history_frame,image=self.delete_photo,hover=False,text='',fg_color = ("#EEEEEE"),text_color='black',command=gen_cmd(key))
            a.grid(row=i,column=8)
            i+=1
        self.history_frame.grid(row=4,column=0,columnspan=5,sticky='ew')        
class edit_ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args,user_id:str, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x500")
        
        try:
            self.title('編輯會員')
            self.user_id=user_id
            self.columnconfigure((0,1),weight=1)
            self.rowconfigure((2,3),weight=2)
            user=get_user(Session(engine),self.user_id)
            edit_n=customtkinter.CTkLabel(self,text='姓名',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n1=customtkinter.CTkLabel(self,text='電話',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n2=customtkinter.CTkLabel(self,text='地址',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n3=customtkinter.CTkLabel(self,text='備註',text_color='black',font=("microsoft yahei", 18, 'bold'))
            self.edit_entry_n=customtkinter.CTkEntry(self)
            self.edit_entry_n1=customtkinter.CTkEntry(self)
            self.edit_entry_n2=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            self.edit_entry_n3=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            
            self.edit_entry_n.insert(END,f'{user.Name}')
            self.edit_entry_n1.insert(END,f'{user.Phone}')
            self.edit_entry_n2.insert(END,f'{user.Address}')
            self.edit_entry_n3.insert(END,f'{user.Remark}')
            self.cancel_bt=customtkinter.CTkButton(self,text='取消',command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
            confirm_bt=customtkinter.CTkButton(self,text='確定更改',command=self.confirm_edit,font=("microsoft yahei", 18, 'bold'))
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
            self.title('錯誤')
            error_label=customtkinter.CTkLabel(self,text='查詢失敗，請回上層進行查詢',font=("microsoft yahei", 18, 'bold'))
            error_bt=customtkinter.CTkButton(self,text='回上層',command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
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
            self.title('新增會員')
            self.columnconfigure((0,1),weight=1)
            self.rowconfigure((3,4),weight=2)
            
            edit_n=customtkinter.CTkLabel(self,text='姓名',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n1=customtkinter.CTkLabel(self,text='電話',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n2=customtkinter.CTkLabel(self,text='地址',text_color='black',font=("microsoft yahei", 18, 'bold'))
            edit_n3=customtkinter.CTkLabel(self,text='備註',text_color='black',font=("microsoft yahei", 18, 'bold'))
            # edit_n4=customtkinter.CTkLabel(self,text='廠商編號',text_color='black')
            self.edit_entry_n=customtkinter.CTkEntry(self)
            self.edit_entry_n1=customtkinter.CTkEntry(self)
            self.edit_entry_n2=customtkinter.CTkTextbox(self,border_color='black',border_width=2)
            self.edit_entry_n3=customtkinter.CTkTextbox(self,border_color='black',border_width=2)

            self.cancel_bt=customtkinter.CTkButton(self,text='取消',command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
            confirm_bt=customtkinter.CTkButton(self,text='確定新增',command=self.confirm_edit,font=("microsoft yahei", 18, 'bold'))
            self.cancel_bt.grid(row=5,column=0,sticky='e',padx=30,pady=10)
            confirm_bt.grid(row=5,column=1,sticky='e',padx=30,pady=10)
            edit_n.grid(row=1,column=0)#姓名
            edit_n1.grid(row=2,column=0)#電話
            edit_n2.grid(row=3,column=0)#地址
            edit_n3.grid(row=4,column=0)#備註
            
            self.edit_entry_n.grid(row=1,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n1.grid(row=2,column=1,sticky='ew',padx=10,pady=10)
            self.edit_entry_n2.grid(row=3,column=1,sticky='nsew',padx=10,pady=10)
            self.edit_entry_n3.grid(row=4,column=1,sticky='nsew',padx=10,pady=10)
            
        except:
            error_label=customtkinter.CTkLabel(self,text='查詢失敗，請回上層進行查詢',font=("microsoft yahei", 18, 'bold'))
            error_bt=customtkinter.CTkButton(self,text='回上層',command=self.cancel_click,font=("microsoft yahei", 18, 'bold'))
            error_label.pack(anchor='center',fill='y',pady=30)
            error_bt.pack(anchor='center',fill='y',pady=10)
    def cancel_click(self):
        self.destroy()
    def confirm_edit(self):
        try:
            add_data(Session(engine),name=self.edit_entry_n.get(),phone=self.edit_entry_n1.get(),address=self.edit_entry_n2.get(1.0,END),remark=self.edit_entry_n3.get(1.0,END))
            self.destroy()
            tk.messagebox.showinfo(title='新增成功', message="新增成功", )
        except:
            tk.messagebox.showinfo(title='新增失敗', message="新增失敗", )


        