from tkinter import *

# s262-1-1-1 创建window，以及window的标题，四周边框
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

# s262-1-1-2 创建背景图片的canvas
canvas = Canvas(width=100,height=100)
image = PhotoImage(file="sun.png")
# s262-1-1-3 定位图片在canvas的位置
canvas.create_image(50,50,image=image)
canvas.grid(column=1,row=0)

webset_label = Label(text="Website",font=("Courier",20,"bold"))
webset_label.config(padx=10,pady=10)
webset_label.grid(column=0,row=1)

email_label = Label(text="Email/Username",font=("Courier",20,"bold"))
email_label.config(padx=10,pady=10)
email_label.grid(column=0,row=2)

pwd_label = Label(text="Password",font=("Courier",20,"bold"))
pwd_label.config(padx=10,pady=10)
pwd_label.grid(column=0,row=3)

# s264-1-1-1 创建数据框，注意columnspan参数是横跨两个格子
input1 = Entry(width=35)
input1.grid(column=1,row=1,columnspan=2)

input2 = Entry(width=35)
input2.grid(column=1,row=2,columnspan=2)

input3 = Entry(width=16)
input3.grid(column=1,row=3)


button1 = Button(text="Generate Password")
button1.grid(column=2,row=3)

# s264-1-1-2 添加按钮，注意也是columnspan=2
button2 = Button(text="Add",width=35)
button2.grid(column=1,row=4,columnspan=2)

window.mainloop()