import os
import time
import customtkinter
from sql_app.database import engine,Base,sessionmaker
import tkinter as tk
class backup_Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bt_frame=customtkinter.CTkFrame(self,fg_color='#EEEEEE')

        self.backup_bt=customtkinter.CTkButton(self.bt_frame,text="備份",command=self.backup)
        
        self.restore_bt=customtkinter.CTkButton(self.bt_frame,text='恢復',command=self.restore)

        self.backup_bt.pack(side='left',padx=20)
        self.restore_bt.pack(side='left',padx=20)
        self.bt_frame.pack(pady=50,padx=20,anchor='n',fill='x')
    def backup(self):
        DB_HOST = 'localhost'
        DB_USER = 'postgres'
        DB_PASS = '1234'
        DB_NAME = 'first_data'


        TIMESTAMP = time.strftime('%Y-%m-%d-%H-%M-%S')
        BACKUP_FILE = DB_NAME + '_' + TIMESTAMP + '.sql'
        BACKUP_PATH = customtkinter.filedialog.asksaveasfilename(defaultextension='.sql',filetypes=[('自訂檔','.sql')],initialfile=f'{BACKUP_FILE}')



        BACKUP_CMD = f"pg_dump --dbname=postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME} > {BACKUP_PATH} "
        os.system(BACKUP_CMD)
        tk.messagebox.showinfo(title='成功', message="備份成功", )
        # os.path.join(BACKUP_PATH, BACKUP_FILE)
    def restore(self):
        sessionmaker.close_all()
        Base.metadata.drop_all(engine)
        DB_HOST = 'localhost'
        DB_USER = 'postgres'
        DB_PASS = '1234'
        DB_NAME = 'first_data'
        restore_PATH = customtkinter.filedialog.askopenfilename()
        restore_CMD=f'psql --dbname=postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME} -f {restore_PATH}'
        os.system(restore_CMD)
        tk.messagebox.showinfo(title='成功', message="恢復成功", )