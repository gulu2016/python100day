from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time

# s197-1-1-1 设置屏幕的属性
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
# s198-1-1-2 关闭动画，手动更新动画
screen.tracer(0)

ball = Ball()

# s198-1-1-1 创建paddle对象
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)

# s198-1-1-3 按上下键执行的函数
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(),new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(),new_y)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

# s199-1-2-1 在main函数中监听左右paddle的动作
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

# s198-1-1-4 游戏启动时候就是不断刷新动画
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()
