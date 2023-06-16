from turtle import Turtle

# s204-1-2-1 Scoreboard就是用来记录分数的
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboared()

    # s204-1-2-2 更新分数，写到固定位置尚
    def update_scoreboared(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))

    # s204-1-2-3 当两边有一方得分的时候，更新分数
    def l_point(self):
        self.l_score += 1
        self.update_scoreboared()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboared()



