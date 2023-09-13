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
import tkinter as tk

class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root, width=200, height=200, bg='red')
        self.hide_button = tk.Button(self.root, text='隱藏', command=self.hide_frame)
        self.show_button = tk.Button(self.root, text='顯示', command=self.show_frame)

        self.frame.pack()
        self.hide_button.pack(side='left')
        self.show_button.pack(side='left')

    def hide_frame(self):
        self.frame.pack_forget()

    def show_frame(self):
        self.frame.pack()

    def run(self):
        self.root.mainloop()

Example().run()

    
