from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DIRECT_HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_back_start_point()
        # s211-1-1-1 设定乌龟的朝向为正上方
        self.setheading(DIRECT_HEADING)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def go_back_start_point(self):
        self.goto(STARTING_POSITION)