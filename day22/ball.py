from turtle import Turtle

# s200-1-1-1 创建Ball类
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    # s201-1-1-1 如果碰到上下墙壁了，那么就会改变y_move的方向
    def bounce_y(self):
        self.y_move *= -1

    # s204-1-3-1 当球被接到的时候，通过减少move_speed来缩短刷新时间
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # s203-1-1-1 重置ball的位置，并且改变移动方向
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()