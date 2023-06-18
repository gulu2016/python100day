import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# s211-1-2-3 关闭自动更新动画
screen.tracer(0)

player = Player()
car_manager = CarManager()

# s211-1-2-1 监听屏幕，如果是按下向上键，那么就执行go_up函数
screen.listen()
screen.onkey(player.go_up,"Up")

level_board = Scoreboard()

game_is_on = True
while game_is_on:
    # s211-1-2-2 screen.update是按时手动更新动画
    time.sleep(0.1)
    screen.update()
    level_board.update_scoreboared()
    # s212-1-2-1 随机生成一些car，这里添加一些随机数减少生成的频率
    car_manager.createCar(random.choice([0,0,0,0,0,0,0,1]))
    car_manager.move_cars()

    # s213-1-1-1 使用car检测是否和player相碰撞
    # s213-1-1-2 问题：为什么使用 player.distance(car) 没有生效？
    for car in car_manager.carList:
        if car.distance(player) < 20:
            game_is_on = False
            level_board.print_game_over()

    # s213-1-1-1 如果到达了终点，那么就增加car的移动速度，player重新回到起点
    if player.ycor() > 300:
        car_manager.increase_speed()
        player.go_back_start_point()
        level_board.upgrade_level()



screen.exitonclick()