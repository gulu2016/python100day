from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

# s191-1-1-1 创建scoreboard类，记录分数
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # s191-1-1-2 设置计分板的初始分数，颜色，位置
        self.score = 0
        # s220-1-1-1 从文件中读取最高分
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # s191-1-1-3 更新计分板内容
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # s220-1-1-2 将最高分写入文件中
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()




