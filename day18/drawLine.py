import turtle as t

tom = t.Turtle()

# s167-1-1-1 画虚线就是利用penup和pendown的组合
for _ in range(15):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = t.Screen()
screen.exitonclick()
