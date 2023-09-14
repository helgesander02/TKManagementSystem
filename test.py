from sqlalchemy.orm import Session
from sqlalchemy import text
from sql_app.database import engine,Base
from sql_app.crud import *
import pandas as pd
import os
import customtkinter
import os
from PIL import Image
from tkinter import *
import datetime
import tkinter as tk
import os
import time
import sqlalchemy as sa
# import os


Base.metadata.drop_all(engine)
DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_PASS = '1234'
DB_NAME = 'new'
restore_PATH = customtkinter.filedialog.askopenfilename()
restore_CMD=f'psql --dbname=postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME} -f {restore_PATH}'
os.system(restore_CMD)

