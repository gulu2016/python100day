from tkinter import *
import math
#--------------------------------- CONSTANTS ------------------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ------------------------ Reset --------------------------------------------------#
def reset_timer():
    #s260-1-1-1 点击reset自会后，取消timer的刷新，timer就是负责倒计时的对象
    window.after_cancel(timer)
    # s260-1-1-2 重置canvas,timer_label，finish_label对象的text
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer")
    finish_label.config(text="")
    # s260-1-1-3 重置reps
    global reps
    reps = 0


# ---------------------------- Timer ------------------------------------------------------ #
# s257-1-1-4 添加button触发的函数，点击start就开始从指定的分钟倒计时
def strat_timer():
    global  reps
    reps += 1

    # s259-1-1-1 计算不同时长的秒数
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # s259-1-1-2 处于不同的倒计时，有不同的标题
    if reps % 8 == 0:
        count_down(long_break_sec)
        # s259-1-1-3 直接改变timer_label的内容和颜色
        timer_label.config(text="Long Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)

# ------------------------------- COUNTDOWN MECHANISM ---------------------------------------#
def count_down(count):
    global reps
    # s257-1-1-3 倒计时的分钟和秒，计算出来后需要使用floor函数取整
    count_min = math.floor(count/60)
    count_sec = count % 60

    # s258-1-1-1 如果秒数小于10，那么显示时候在其前边多加一个0
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # s257-1-1-2 每次都更新画布上的text，更新倒计时的剩余时间
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    # s257-1-1-1 倒计时功能，每过一秒，就调用count_down，并且传入的count减1
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count - 1)
    else:
        strat_timer()
        if reps % 2 == 1:
            finish_label.config(text="√"*math.floor(reps/2))

# -------------------------------- UI SETUP ------------------------------------------- #
# s255-1-1-1 创建window，配置标题，大小和背景颜色
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# s255-1-1-2 创建画布，并使用图片作为背景板，画布的长宽和背景图片一致
canvas = Canvas(width=1653,height=993,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="FastSession.png")
# s255-1-1-3 在画布的中心位置使用图片
canvas.create_image(827,497,image=image)
# s255-1-1-4 在画布的中心位置设置text
timer_text = canvas.create_text(827,497,text="00:00",fill="blue",font=(FONT_NAME,50,"bold"))
canvas.grid(column=1,row=1)

# s256-1-1-1 添加timer label
timer_label = Label(text="Timer", font=(FONT_NAME,60,"bold"),fg=GREEN,bg=YELLOW)
timer_label.config(padx=10,pady=20)
timer_label.grid(column=1,row=0)

# s256-1-1-2 添加完成的label,fg和bg和其他组件保持一致
finish_label = Label(font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
finish_label.config(padx=10,pady=20)
finish_label.grid(column=1,row=3)

# s256-1-1-3 添加两个button，highlightthickness=0表示没有边框
start_button = Button(text="Start",command=strat_timer,highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_button.grid(column=2,row=2)

window.mainloop()





