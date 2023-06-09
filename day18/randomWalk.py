import turtle as t
import random as r

step_distance = 40
turn_angel = 90
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = ["right","left","forward"]

# s169-1-1-1 设置速度和线条的粗细
tom = t.Turtle()
tom.speed(8)
tom.pensize(5)

for _ in range(200):
    # s169-1-1-2 选取随机的颜色
    tom.color(r.choice(colours))
    tom.forward(step_distance)
    # s169-1-1-3 每次运动完成后要改变方向
    if r.choice(direction) == "right":
        tom.right(r.choice(range(90)))
    elif r.choice(direction) == "left":
        tom.left(r.choice(range(90)))
    else:
        continue

screen = t.Screen()
screen.exitonclick()


