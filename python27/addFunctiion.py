
def add(*args):
    # s248-1-1-1 可变参数传进去实际上是一个tuple
    print(type(args))
    ans = 0
    # s248-1-1-2 遍历所有元素并相加
    for item in args:
        ans += item
    return ans


print(add(1,2,3,4,5,6,7))