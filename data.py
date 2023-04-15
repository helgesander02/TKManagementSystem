import tkinter as tk
import customtkinter
from tkcalendar import DateEntry
# Data () 數據
class Data_Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        bt_=button_Frame(self,fg_color=("#EEEEEE"))
        bt_.pack(pady=40,padx=40,anchor='nw')
        a=customtkinter.CTkFrame(self)
        date_label=customtkinter.CTkLabel(a,text='日期')
        date1=DateEntry(a,selectmode='day')
        date2=DateEntry(a,selectmode='day')
        date_label.grid(row=0,column=0)
        date1.grid(row=0,column=1,padx=30)
        date2.grid(row=1,column=1,padx=30)
        a.pack(anchor='w',padx=30,fill='x')
        b=customtkinter.CTkFrame(self)
        b.columnconfigure((0,1),weight=1)
        b.rowconfigure((0,1),weight=1)
        label1=customtkinter.CTkLabel(b,text='利潤分析')
        label2=customtkinter.CTkLabel(b,text='會員分析')
        label3=customtkinter.CTkLabel(b,text='通路分析')
        label4=customtkinter.CTkLabel(b,text='品項分析')
        label1.grid(row=0,column=0,sticky='nw')
        label2.grid(row=0,column=1,sticky='nw')
        label3.grid(row=1,column=0,sticky='nw')
        label4.grid(row=1,column=1,sticky='nw')
        b.pack(anchor='w',padx=30,pady=30,fill='both',expand=1)
class button_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        #5b5a5a
        self.input_button = customtkinter.CTkButton(self, text="數據分析", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.input_button.grid(row=0, column=5,padx=30)
        self.edit_button = customtkinter.CTkButton(self, text="其他...", width=150, height=40,
                                                        fg_color=("#EEEEEE"),
                                                        font=("microsoft yahei", 18, 'bold'),
                                                        text_color='black',border_width=2,corner_radius=0,
                                                        hover_color='#5b5a5a')
        self.edit_button.grid(row=0, column=6,padx=30)


    def reset_color(self):
        self.input_button.configure(fg_color = ("#EEEEEE"),text_color='black')
        self.edit_button.configure(fg_color = ("#EEEEEE"),text_color='black')