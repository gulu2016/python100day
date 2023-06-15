from turtle import Turtle

# s199-1-1-1 单独创建paddle类，继承Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5,stretch_len=1)
        paddle.penup()
        paddle.goto(position)

    # s199-1-1-2 定义上下移动的函数，但是目前测试发现不会移动
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

