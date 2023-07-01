from tkinter import *

window = Tk()

# s246-1-1-1 定义window和窗体自带的title
window.title("My First GUI Program")
window.minsize(width=580,height=380)
# s252-1-1-5 给整个window设置一个边缘，这样组件不会紧贴着四周
window.config(padx=20,pady=20)

# s246-1-1-2 定义在window中显示的label，并定义位置
my_label = Label(text="I Am a Label", font=("Arial",24,"bold"))
# s252-1-1-4 pack是按照上下左右四个方向给组件定位的，只能粗略控制
# my_label.pack()
# s252-1-1-3 place是按照坐标给组件定位的
# my_label.place(x=0,y=0)
# s252-1-1-6 给组件四周设置边缘，这样组件之间也会有间隔
my_label.config(padx=100,pady=200)
my_label.grid(column=0,row=0)



# button
def button_clicked():
    print("I got clicked")
    # s250-1-1-3 更新my_label，变为新的内容
    my_label.config(text="Button clicked")
    # s250-1-1-6 将输入框中的内容替换my_label内容
    my_label.config(text=input.get())

# s250-1-1-1 定义button上显示的文本，点击后触发的函数
button = Button(text="click me",command=button_clicked)
# s250-1-1-2 如果要在屏幕上显示，那么需要调用pack函数
# button.pack()
# s252-1-1-1 grid是按照相对位置给所有组件排序的
# s252-1-1-2 有了grid之后，是不能再使用pack函数的
button.grid(column=0,row=1)


# entry
# s250-1-1-4 定义输入框
input = Entry(width=10)
# s250-1-1-5 显示到屏幕上
#input.pack()
print(input.get())
input.grid(column=1,row=0)


#Text
# s251-1-1-1 定义文本输入框
text = Text(height=5, width=30)
#Puts cursor in textbox.
# s251-1-1-2 设置输入光标
text.focus()
#Adds some text to begin with.
# s251-1-1-3 自带的文字
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
# s251-1-1-4 在第1行，第0个字符插入END标识符
print(text.get("1.0", END))
#text.pack()
text.grid(column=2,row=0)

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
# s251-1-1-5 设置可以上下调整的输入框，每次点击上或下，都会调用spinbox_used函数
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
spinbox.grid(column=3,row=0)

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
# s251-1-1-6 点击可以滑动的进度条，每次改变都会调用scale_used函数
scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
scale.grid(column=4,row=0)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# s251-1-1-7 勾选框，0标识没有勾选，1标识已经勾选，每次改变都会调用checkbutton_used函数
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()
checkbutton.grid(column=5,row=0)

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
# s251-1-1-8 圆圈按钮，多个选项中选一个，每次改变都会调用radio_used函数
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
#radiobutton1.pack()
#radiobutton2.pack()
radiobutton1.grid(column=6,row=0)
radiobutton2.grid(column=6,row=1)


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
# s251-1-1-9 选项列表，每次改变都会调用listbox_used函数，这里<<ListboxSelect>>好像是固定写法
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
listbox.grid(column=7,row=0)



# s246-1-1-3 保持window一直显示
window.mainloop()














