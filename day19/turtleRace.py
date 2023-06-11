import random
from turtle import Turtle,Screen
import random as r

tim = Turtle()
screen = Screen()
# s179-1-1-1 设定屏幕的尺寸
screen.setup(width=500,height=400)
# s179-1-1-2 设置输入框，并给出提示文字
userinput = screen.textinput(title="make your bet",prompt="which turtl will win the race")
colors = ["red","orange","yellow","green","blue","purple"]
y_p = [-70,-40,-10,20,50,80]
turtles = []
is_race_on = False

for i in range(0,6):
    # s179-1-1-3 指定turtle的外形和颜色
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    # s179-1-1-4 指定tutle到指定的位置
    tim.goto(x=-230,y=y_p[i])
    turtles.append(tim)

# s180-1-1-1 判断用户有输入就开始比赛
if userinput:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        # s180-1-1-2 如果一半超过屏幕就停止比赛
        if(turtle.xcor() > 230):
            is_race_on = False
            if turtle.pencolor() == userinput:
                print("you are right")
            else:
                print(f"you are wrong, the right one is {turtle.pencolor()}")
            break
        # s180-1-1-3 每次向前移动一个[0,10]的长度
        turtle.forward(random.randint(0,10))



screen.exitonclick()



