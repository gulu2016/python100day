import tkinter

window = tkinter.Tk()

# s246-1-1-1 定义window和窗体自带的title
window.title("My First GUI Program")
window.minsize(width=580,height=380)

# s246-1-1-2 定义在window中显示的label，并定义位置
my_label = tkinter.Label(text="I Am a Label", font=("Arial",24,"bold"))
my_label.pack()

# s246-1-1-3 保持window一直显示
window.mainloop()














