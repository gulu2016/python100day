from turtle import Turtle,Screen

timmy_turtul = Turtle()
# s164-1-1-2 定义形状
timmy_turtul.shape("turtle")
# s164-1-1-1 颜色的选择可以参考https://trinket.io/docs/colors
timmy_turtul.color("aquamarine")
# s164-1-1-3 定义移动的距离和方向
#timmy_turtul.forward(100)
#timmy_turtul.right(90)
#timmy_turtul.forward(20)

# s165-1-1-1 画一个正方形
timmy_turtul.forward(200)
timmy_turtul.right(90)
timmy_turtul.forward(200)
timmy_turtul.right(90)
timmy_turtul.forward(200)
timmy_turtul.right(90)
timmy_turtul.forward(200)
timmy_turtul.right(90)

screen = Screen()
screen.exitonclick()