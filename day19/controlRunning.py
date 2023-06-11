from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def mov_forwards():
    tim.forward(10)

def mov_backwards():
    tim.backward(10)

def mov_turnright():
    tim.right(10)

def mov_turnleft():
    tim.left(10)

def screen_clear():
    # s177-1-1-2 使用tim的clear而不是screen的clear(screen的clear会把箭头也清理掉)
    # s177-1-1-3 使用penup和pendown避免回到原点时候留下痕迹
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

# s177-1-1-1 编写键盘监听函数，不同按键调用不同函数
screen.onkey(key="w",fun=mov_forwards)
screen.onkey(key="s",fun=mov_backwards)
screen.onkey(key="d",fun=mov_turnright)
screen.onkey(key="a",fun=mov_turnleft)
screen.onkey(key="c",fun=screen_clear)
screen.exitonclick()
