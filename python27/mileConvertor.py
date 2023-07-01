from tkinter import *


window = Tk()
# s253-1-1-1 创建window
window.title("Mile to Km Converter")
window.minsize(width=580,height=380)
window.config(padx=100,pady=100)

# s253-1-1-2 创建需要的组件，并且使用grid按照位置相对排序
input1 = Entry(width=10)
print(input1.get())
input1.grid(column=1,row=0)

miles = Label(text="Miles", font=("Arial",24,"bold"))
miles.config(padx=10,pady=10)
miles.grid(column=2,row=0)

text1 = Label(text="is equal to", font=("Arial",24,"bold"))
text1.config(padx=10,pady=10)
text1.grid(column=0,row=1)

text2 = Label(text="0", font=("Arial",24,"bold"))
text2.config(padx=10,pady=10)
text2.grid(column=1,row=1)

km = Label(text="Km", font=("Arial",24,"bold"))
km.config(padx=10,pady=10)
km.grid(column=2,row=1)

# s253-1-1-3 实现点击button之后需要实现的函数
def button_clicked():
    print("I got clicked")
    input_miles = int(input1.get())
    output_km = input_miles*1.6
    text2.config(text = output_km)

# s253-1-1-4 定义button
button = Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()