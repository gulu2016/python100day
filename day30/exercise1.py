fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    # s271-1-1-1 使用try来执行可能报错的部分
    try:
        fruit = fruits[index]
    # s271-1-1-2 这里只捕获IndexError
    except IndexError:
        print("Fruit pie")
    # s271-1-1-3 如果没有error，就执行else部分
    else:
        print(fruit+" pie")

make_pie(4)