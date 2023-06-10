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
# s170-1-1-1 如果要使用RGB颜色，需要设置t.colormode(255)
t.colormode(255)

# s170-1-1-2 拼装rgb颜色的函数，返回的是一个tuple
def random_color():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    return (red,green,blue)

for _ in range(200):
    # s169-1-1-2 选取随机的颜色,使用颜色列表中的颜色
    # tom.color(r.choice(colours))
    # s170-1-1-3 选取随机的颜色，使用的是随机拼装的rgb颜色
    tom.color(random_color())
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


