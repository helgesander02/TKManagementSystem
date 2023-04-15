from tkinter import *
from tkinter import ttk

def show_btn(pathname, value):
	print (pathname)
	print (value)
	pathname.insert(END, value)

def main_gui():
	def gen_cmd(i):return lambda:show_btn(en_1,i)
	win =Tk()
	en_1=ttk.Entry(win)
	en_1.pack()
	for i in range(1,11):
		btn_i=ttk.Button(win,text=i,command=gen_cmd(i))
		btn_i.pack()
	win.mainloop()
main_gui()
