from sqlalchemy.orm import Session
import sqlalchemy as sa
from sql_app.database import engine
from sql_app.crud import *
import pandas as pd
import os
import customtkinter
import os
from PIL import Image
from tkinter import *
import datetime
file_path = customtkinter.filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
df=pd.read_excel(file_path)
for index,row in df.iterrows():
    print(index)
    
