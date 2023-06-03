# s146-1-1-1 两种引入类的方式
# import turtle
# from turtle import Turtle

from turtle import Turtle,Screen
# s146-1-1-2 构造对象的方式就是直接Turtle()
timmy = Turtle()
print(timmy)
# s146-1-1-4 调用Turtle类的函数
timmy.shape("turtle")
timmy.color("pink")
timmy.forward(100)
timmy.right(20)
timmy.forward(100)

screen = Screen()
print(screen.window_width())
# s146-1-1-3 调用函数，只有点击的时候才会退出窗口
screen.exitonclick()