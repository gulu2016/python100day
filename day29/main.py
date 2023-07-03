from tkinter import *

# s262-1-1-1 创建window，以及window的标题，四周边框
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# s262-1-1-2 创建背景图片的canvas
canvas = Canvas(width=1000,height=1000)
image = PhotoImage(file="sun.png")
# s262-1-1-3 定位图片在canvas的位置
canvas.create_image(500,500,image=image)
canvas.grid(column=1,row=1)

window.mainloop()