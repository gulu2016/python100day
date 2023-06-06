import turtle as t
import random as r

# s168-1-1-1 turtle不同的颜色
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tom = t.Turtle()
lineLen = 80

def drawShape(lineNum):
    angle = int(360 / lineNum)
    for j in range(lineNum):
        tom.forward(lineLen)
        tom.right(angle)

for i in range(3,20):
    lineNum = i
    # s168-1-1-2 使用random随机选取不同的颜色
    tom.color(r.choice(colours))
    drawShape(lineNum)



screen = t.Screen()
screen.exitonclick()
