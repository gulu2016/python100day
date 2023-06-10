import turtle as t
import random as r

def random_color():
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    return (red,green,blue)

# s171-1-1-1 设置每次旋转的角度以及总次数
turn_angle = 5
turn_times = int(360/turn_angle)
t.colormode(255)

# s171-1-1-2 设置turtle的基本信息
tom = t.Turtle()
tom.home()
tom.speed(0)
tom.pensize(2)

# s171-1-1-3 画图，circle的参数指定半径，left指定旋转位置，也可以用setheading函数
for _ in range(turn_times):
    tom.color(random_color())
    tom.circle(140)
    tom.left(turn_angle)



screen = t.Screen()
screen.exitonclick()










