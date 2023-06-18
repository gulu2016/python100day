from turtle import Turtle

# s185-1-1-1 将可能更改的设置为常量，放到文件头，这样好控制
START_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVINT_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


# s185-1-1-2 创建snake类，内容就是从main搬过来的
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        # s186-1-2-1 定义snake的头
        self.head = self.segment[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    # s193-1-1-1 增加身体模块的函数
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    # s193-1-1-2 延长身体的长度，找到最后一个节点的位置
    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVINT_DISTANCE)

    # s186-1-2-2 移动的函数，设定方向用setheading，目前的方向是heading
    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def reset(self):
        for seg in self.segment:
            self.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
