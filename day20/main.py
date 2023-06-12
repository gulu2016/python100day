from turtle import Turtle,Screen
import time

screen = Screen()
# s183-1-1-1 创建屏幕，设置背景和标题
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# s183-1-1-2 设置snake的初始位置
starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

# s183-1-1-3 三个位置创建方块，定义Turtle的形状，颜色和位置
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    # s184-1-1-1 每次所有方块都移动好之后，screen再update
    screen.update()
    # s184-1-1-2 延时
    time.sleep(0.1)
    for seg_num in range(len(segments) -1, 0, -1):
        # s184-1-1-3 更新turtle位置，后一个覆盖前一个位置，第一个会走到新位置
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)


screen.exitonclick()



