class User:
    #s153-1-1-1 如果暂时跳过，可以使用pass关键字
    #pass
    # s154-1-1-2 定义构造函数，self表示当前对象
    def __init__(self,userId,userName):
        # s154-1-1-3 使用参数给对象的属性赋值
        self.userId = userId
        self.userName = userName
        # s154-1-1-4 如果给对象的属性默认值，那么在调用构造函数时候可以不用给值
        self.follower = 0
        self.following = 0

    # s155-1-1-1 定义函数
    def follow(self,user):
        user.follower += 1
        self.following += 1

# s154-1-1-6 有了构造函数之后，就不可以调用空构造函数了
#user_1 = User()

#s154-1-1-1 即使类中没有该属性，也可以直接定义属性并给属性赋值
#user_1.id = "001"
#user_1.name = "abc"

# s154-1-1-5 调用对象的构造函数
user_2 = User("001","abc")
print(user_2.follower)

user_3 = User("003","bcd")
user_2.follow(user_3)
print(user_2.follower)
print(user_2.following)
print(user_3.follower)
print(user_3.following)



