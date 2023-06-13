from turtle import  Turtle
import random

# s190-1-1-1 创建food类，继承Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        # s190-1-1-2 定义形状，尺寸，颜色以及移动的速度
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # s190-1-1-3 随机刷新到下一个位置的函数
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


