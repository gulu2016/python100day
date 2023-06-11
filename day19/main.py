from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def mov_forwards():
    tim.forward(10)

# s176-1-1-1 监听按键的函数
screen.listen()
# s176-1-1-2 如果按下space，那么就会调用mov_forwards
# s176-1-1-3 mov_forwards是高阶函数，能够接收函数作为参数
screen.onkey(key="space",fun=mov_forwards)
screen.exitonclick()

