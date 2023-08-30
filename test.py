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
a=date_search(Session(engine),'2000-1-1','2023-8-23')

    
