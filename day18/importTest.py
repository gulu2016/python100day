# s166-1-1-1 第一种引用形式：import xxx
#import turtle
# s166-1-1-2 使用时候要带上包名
#tim = turtle.Turtle()

# s166-1-1-3 第二种引用形式：from turtle import Turtle
#from turtle import Turtle
# s166-1-1-4 使用时候直接使用类名
# tim = Turtle()

# s166-1-1-5 第三种引用形式：from turtle import *，引用包内所有内容
#from turtle import *
# s166-1-1-6 使用时候直接使用类名,但是这种方式在代码比较长的时候不容易知道Turtle是来自哪个包
#tim = Turtle()

# s166-1-1-7 第四种引用形式：import turtle as t，给包起别名
import turtle as t
# s166-1-1-8 使用时候直接使用别名
tim = t.Turtle()

# s166-1-1-9 对于非内置的python包，需要安装后使用
import heroes
print(heroes.gen())
