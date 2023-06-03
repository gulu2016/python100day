from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



is_on = True
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
while is_on:

    # s149-1-1-1 使用面向对象方式重写，主要是引入对应的对象
    # 调用对象的方法完成任务，通过对象的属性连接任务
    choice = input(f"​What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeeMaker.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)