from tkinter import *

root = Tk()

# 創建 Frame
frame = Frame(root)
frame.pack()

# 創建初始的 Label
label = Label(frame, text="這是初始的內容")
label.pack()
label1 = Label(frame, text="2")
label1.pack()

# 創建更新按鈕，點擊時會更新 Label 的內容
def update_label():
    # 更新 Label 的內容
    label.config(text="這是更新後的內容")
    # 使用 pack() 方法重新放置 Label
    label.pack()

button = Button(root, text="更新", command=update_label)
button.pack()

root.mainloop()

