import customtkinter
from PIL import Image
from tkcalendar import DateEntry
from sql_app.crud import *
from sqlalchemy.orm import Session
from sql_app.database import engine
from .floatspinbox import FloatSpinbox,sum_Frame
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

