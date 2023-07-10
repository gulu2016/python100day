from tkinter import *
# s266-1-1-1 添加messagebox，需要单独导入
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# s274-1-1-1 json是内置的python包，不需要安装
import json

# -------------------- password generator --------- #
def generator_password():
    # s267-1-1-1 创建随机数列表
    letters = ['a','b','c','d','e','f','g']
    numbers = ['0','1','2','3','4']
    symbols = ['!','@','#','$','%','^']
 
    # s267-1-1-2 选取随机个数的字符
    password_letters = [choice(letters) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    # s267-1-1-3 shuffle会将字符串列表打乱
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # s267-1-1-4 连接字符串的简单方式
    password = "".join(password_list)
    # s267-1-1-5 将生成的密码填入password中
    input3.insert(0,password)
    # s267-1-1-6 将生成的密码写入剪贴板中
    pyperclip.copy(password)

# ----------------
def save():
    # s265-1-1-4 获取输入框中的内容
    website = input1.get()
    email = input2.get()
    password = input3.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    # s266-1-1-2 如果有字段为空，弹出警告的对话框showinfo
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="don't leave email or password empty")
    else:
        # s266-1-1-3 填好信息后，弹出确认对话框askokcancel
        is_ok = messagebox.askokcancel(title=website,
                                   message=f"These are the details entered: \n Email:{email} "
                                   f"\nPassword:{password} \nIs it ok to save?")
        if is_ok:
            # s265-1-1-5 将输入框中的内容保存到文件
            # with open("my_file.txt",mode="a") as file:
            # s275-1-1-1 添加处理异常的逻辑
            try:
                with open("data.json", mode="r") as data_file:
                    #file.write("\n")
                    #file.write(f"{website} | {email} | {password}")
                    # s274-1-1-2 从json中读取数据
                    data = json.load(data_file)
            # s275-1-1-2 如果读不到文件，那么就新建文件
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            # s275-1-1-3 读到文件就正常更新
            else:
                # s274-1-1-3 更新读到的内容
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # s274-1-1-4 将数据写到json文件中
                    json.dump(new_data, data_file, indent=4)
            # s275-1-1-4 最终都要删除输入框中的内容
            finally:
                # s265-1-1-6 保存之后，将内容删除
                input1.delete(0,END)
                input3.delete(0,END)
# ---------------


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
# s265-1-1-3 输入框中带有光标
input1.focus()
input1.grid(column=1,row=1,columnspan=2)

input2 = Entry(width=35)
# s265-1-1-2 输入框中的初始文字
input2.insert(0,"jjj")
input2.grid(column=1,row=2,columnspan=2)

input3 = Entry(width=16)
input3.grid(column=1,row=3)


button1 = Button(text="Generate Password",command=generator_password)
button1.grid(column=2,row=3)

# s264-1-1-2 添加按钮，注意也是columnspan=2
# s265-1-1-1 点击按钮会触发save函数
button2 = Button(text="Add",width=35,command=save)
button2.grid(column=1,row=4,columnspan=2)

window.mainloop()