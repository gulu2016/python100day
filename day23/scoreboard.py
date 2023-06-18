from turtle import Turtle

FONT = ("Courier", 12, "normal")

# s215-1-1-1 创建计分板
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.print_str = "Level: "

    # s215-1-1-2 更新计分板，每次都需要clear上次的写入结果
    def update_scoreboared(self):
        self.clear()
        self.goto(-250,250)
        self.write(self.print_str + str(self.level),align="center",font=FONT)

    # s215-1-1-3 升级，更新写入的内容
    def upgrade_level(self):
        self.level += 1

    # s215-1-1-4 当游戏结束时候，打印内容
    def print_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
