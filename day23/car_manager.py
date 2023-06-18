from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_HEADING = 180

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.carList = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    # s212-1-1-4 需要将create_car和move_car分成两个函数，各司其职
    def createCar(self,car_num):
        for _ in range(car_num):
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            # s212-1-1-1 设置方框的长宽，这里的参数是默认参数的倍数，不是绝对长度和绝对宽度
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()

            # s212-1-1-2 随机生成car的位置
            random_y = random.randint(-250,250)
            car.goto(300,random_y)
            self.carList.append(car)

    # s212-1-1-3 向左边移动就调用backward
    def move_cars(self):
        for car in self.carList:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT


