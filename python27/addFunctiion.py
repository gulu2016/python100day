
def add(*args):
    # s248-1-1-1 可变参数传进去实际上是一个tuple
    print(type(args))
    ans = 0
    # s248-1-1-2 遍历所有元素并相加
    for item in args:
        ans += item
    return ans


print(add(1,2,3,4,5,6,7))


def calculate(n,**kwargs):
    # s249-1-1-1 **是关键字参数，传进来的相当于一个字典
    print(kwargs)
    # s249-1-1-2 使用[]的前提是一定要传入该关键字，否则报错
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        # s249-1-1-3 使用get方法，如果关键字没有传入，会返回none
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissa")
print(my_car.make,my_car.model)