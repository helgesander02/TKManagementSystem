import customtkinter
import datetime
from sql_app.crud import Search_receipt,add_receipt,sum_receipt_money,get_edit_od
from sqlalchemy.orm import Session
from sql_app.database import engine
import tkinter as tk
class acount(customtkinter.CTkFrame):
    def __init__(self, master,selected, **kwargs):
        super().__init__(master, **kwargs)
        print(selected)
        self.selected=selected
        self.key_=list(selected.keys())
        self.i=0
        recipit_=Search_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
        self.left=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.o_id_=customtkinter.CTkLabel(self.left,text=f'訂單編號{self.key_[self.i]}')
        self.m_id_=customtkinter.CTkLabel(self.left,text=f'會員編號{self.selected[self.key_[self.i]]}')
        o_bt=customtkinter.CTkButton(self.left,text='查看訂單細節')
        self.bt=customtkinter.CTkFrame(self.left)
        next_bt=customtkinter.CTkButton(self.bt,text='下一筆',command=self.next_)
        previous_bt=customtkinter.CTkButton(self.bt,text='上一筆',command=self.previous_)
        self.o_id_.pack(anchor='n',padx=15,pady=5)
        self.m_id_.pack(anchor='n',padx=15,pady=5)
        o_bt.pack(anchor='n',padx=15,pady=5)
        previous_bt.grid(row=0,column=0,padx=15,pady=5)
        next_bt.grid(row=0,column=1,padx=15,pady=5)
        self.bt.pack(side='bottom',padx=15,pady=5)
        self.left.pack(side='left',anchor='n',fill='both',padx=10,pady=10)



        self.ac_now_=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.ac_now_.columnconfigure((0,1,2,3,4),weight=1)
        self.ac_now_.pack(fill='x')
        ac_now_title_1=customtkinter.CTkLabel(self.ac_now_,text='收款日期')
        ac_now_title_2=customtkinter.CTkLabel(self.ac_now_,text='收款方式')
        ac_now_title_3=customtkinter.CTkLabel(self.ac_now_,text='收款金額')
        ac_now_title_4=customtkinter.CTkLabel(self.ac_now_,text='折讓')
        ac_now_title_5=customtkinter.CTkLabel(self.ac_now_,text='收款備註')
        ac_now_title_1.grid(row=0,column=0)
        ac_now_title_2.grid(row=0,column=1)
        ac_now_title_3.grid(row=0,column=2)
        ac_now_title_4.grid(row=0,column=3)
        ac_now_title_5.grid(row=0,column=4)
        check_var = customtkinter.StringVar(value=datetime.date.today())
        self.ac_now=customtkinter.CTkScrollableFrame(self,fg_color = ("#EEEEEE"))
        self.ac_now.columnconfigure((0,1,2,3,4),weight=1)
        self.ac_now.pack(fill='both',expand=1)
        self.ac_now_input_1=customtkinter.CTkEntry(self.ac_now,textvariable=check_var,state='disabled')
        self.ac_now_input_2=customtkinter.CTkEntry(self.ac_now)
        self.ac_now_input_3=customtkinter.CTkEntry(self.ac_now,textvariable=customtkinter.IntVar(value=0))
        self.ac_now_input_4=customtkinter.CTkEntry(self.ac_now,textvariable=customtkinter.IntVar(value=0))
        self.ac_now_input_5=customtkinter.CTkEntry(self.ac_now)
        self.ac_now_input_1.grid(row=0,column=0,sticky='ew')
        self.ac_now_input_2.grid(row=0,column=1,sticky='ew')
        self.ac_now_input_3.grid(row=0,column=2,sticky='ew')
        self.ac_now_input_4.grid(row=0,column=3,sticky='ew')
        self.ac_now_input_5.grid(row=0,column=4,sticky='ew')

        self.ac_history_=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.ac_history_.columnconfigure((0,1,2,3,4),weight=1)
        ac_title_1=customtkinter.CTkLabel(self.ac_history_,text='收款日期')
        ac_title_2=customtkinter.CTkLabel(self.ac_history_,text='收款方式')
        ac_title_3=customtkinter.CTkLabel(self.ac_history_,text='收款金額')
        ac_title_4=customtkinter.CTkLabel(self.ac_history_,text='折讓')
        ac_title_5=customtkinter.CTkLabel(self.ac_history_,text='收款備註')
        ac_title_1.grid(row=0,column=0)
        ac_title_2.grid(row=0,column=1)
        ac_title_3.grid(row=0,column=2)
        ac_title_4.grid(row=0,column=3)
        ac_title_5.grid(row=0,column=4)
        self.ac_history_.pack(fill='x')

        sum_,sum_1=sum_receipt_money(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
        self.a=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.a.pack(fill='both',expand=1)
        self.ac_history=customtkinter.CTkScrollableFrame(self.a,fg_color = ("#EEEEEE"),label_text=f'總計：      {0 if sum_==None else sum_}         餘額：      {sum_1-(0 if sum_==None else sum_)}')
        self.ac_history.columnconfigure((0,1,2,3,4),weight=1)
        l=0
        for i in recipit_:
            ac_title_1=customtkinter.CTkLabel(self.ac_history,text=f'{i.date}')
            ac_title_2=customtkinter.CTkLabel(self.ac_history,text=f'{i.m_way}')
            ac_title_3=customtkinter.CTkLabel(self.ac_history,text=f'{i.money}')
            ac_title_4=customtkinter.CTkLabel(self.ac_history,text=f'{i.discount}')
            ac_title_5=customtkinter.CTkLabel(self.ac_history,text=f'{i.remark}')
            ac_title_1.grid(row=l,column=0)
            ac_title_2.grid(row=l,column=1)
            ac_title_3.grid(row=l,column=2)
            ac_title_4.grid(row=l,column=3)
            ac_title_5.grid(row=l,column=4)
            l+=1
        self.ac_history.pack(fill='both',expand=1)

        self.bt=customtkinter.CTkFrame(self,fg_color = ("#EEEEEE"))
        self.ac_bt=customtkinter.CTkButton(self.bt,text='確認入賬',command=lambda:self.add_rc_(m_way=self.ac_now_input_2.get(),money=self.ac_now_input_3.get(),discount=self.ac_now_input_4.get(),remark=self.ac_now_input_5.get()))
        self.reset_ac_bt=customtkinter.CTkButton(self.bt,text='重設入帳',command=self.reset)
        self.ac_bt.pack(side='right',padx=10)
        self.reset_ac_bt.pack(side='right',padx=10)
        self.bt.pack(side='bottom',anchor='e')
    def reset(self):
        self.ac_now_input_2.delete(0,tk.END)
        self.ac_now_input_3.delete(0,tk.END)
        self.ac_now_input_4.delete(0,tk.END)
        self.ac_now_input_5.delete(0,tk.END)
    def next_(self):
        self.i+=1
        self.o_id_.configure(text=f'訂單編號{self.key_[self.i]}')
        self.m_id_.configure(text=f'會員編號{self.selected[self.key_[self.i]]}')
        self.ac_history.pack_forget()
        self.ac_history=customtkinter.CTkScrollableFrame(self.a,fg_color = ("#EEEEEE"))
        self.ac_history.columnconfigure((0,1,2,3,4),weight=1)
        recipit_=Search_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
        l=0
        for i in recipit_:
            ac_title_1=customtkinter.CTkLabel(self.ac_history,text=f'{i.date}')
            ac_title_2=customtkinter.CTkLabel(self.ac_history,text=f'{i.m_way}')
            ac_title_3=customtkinter.CTkLabel(self.ac_history,text=f'{i.money}')
            ac_title_4=customtkinter.CTkLabel(self.ac_history,text=f'{i.discount}')
            ac_title_5=customtkinter.CTkLabel(self.ac_history,text=f'{i.remark}')
            ac_title_1.grid(row=l,column=0)
            ac_title_2.grid(row=l,column=1)
            ac_title_3.grid(row=l,column=2)
            ac_title_4.grid(row=l,column=3)
            ac_title_5.grid(row=l,column=4)
            l+=1
        self.ac_history.pack(fill='both',expand=1)        
    def previous_(self):
        self.i-=1
        self.o_id_.configure(text=f'訂單編號{self.key_[self.i]}')
        self.m_id_.configure(text=f'會員編號{self.selected[self.key_[self.i]]}')
        self.ac_history.pack_forget()
        self.ac_history=customtkinter.CTkScrollableFrame(self.a,fg_color = ("#EEEEEE"))
        self.ac_history.columnconfigure((0,1,2,3,4),weight=1)
        recipit_=Search_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]])
        l=0
        for i in recipit_:
            ac_title_1=customtkinter.CTkLabel(self.ac_history,text=f'{i.date}')
            ac_title_2=customtkinter.CTkLabel(self.ac_history,text=f'{i.m_way}')
            ac_title_3=customtkinter.CTkLabel(self.ac_history,text=f'{i.money}')
            ac_title_4=customtkinter.CTkLabel(self.ac_history,text=f'{i.discount}')
            ac_title_5=customtkinter.CTkLabel(self.ac_history,text=f'{i.remark}')
            ac_title_1.grid(row=l,column=0)
            ac_title_2.grid(row=l,column=1)
            ac_title_3.grid(row=l,column=2)
            ac_title_4.grid(row=l,column=3)
            ac_title_5.grid(row=l,column=4)
            l+=1
        self.ac_history.pack(fill='both',expand=1)
    def add_rc_(self,m_way,money,discount,remark):
        try:           
            add_receipt(db=Session(engine),o_id=self.key_[self.i],m_id=self.selected[self.key_[self.i]],m_way=m_way,money=money,discount=discount,remark=remark)
            tk.messagebox.showinfo(title='入賬成功', message="入賬成功", )
        except:
            tk.messagebox.showinfo(title='入賬失敗', message="入賬失敗", )