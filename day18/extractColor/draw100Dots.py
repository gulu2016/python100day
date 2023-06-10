import colorgram
import turtle as t
import random

step_distance = 60
dot_size = 20

# Extract 6 colors from an image.
colors = colorgram.extract('learn.jpg', 6)
extracted_colors = []
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for color in colors:
    r = int(color.rgb.r)
    g = int(color.rgb.g)
    b = int(color.rgb.b)
    rgb = (r,g,b)
    extracted_colors.append(rgb)

tom = t.Turtle()
tom.home()
tom.speed(0)
# s173-1-1-1 使用数字的rgb颜色一定要设置colormode是255
t.colormode(255)
# s173-1-1-2 设置penup，这样画图不会有直线痕迹
tom.penup()
# s173-1-1-3 将光标隐藏
tom.hideturtle()

# s173-1-1-4 设置点的位置，并在对应位置画一个点
for y in range(0,10):
    tom.sety(y*30)
    for x in range(0,10):
        tom.setx(x*30)
        tom.color(random.choice(colours))
        tom.dot(dot_size)

screen = t.Screen()
screen.exitonclick()