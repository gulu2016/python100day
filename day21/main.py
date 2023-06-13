class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# s189-1-1-1 Fish继承Animal类
class Fish(Animal):
    # s189-1-1-2 Fish的init函数会先调用父类的init函数
    def __init__(self):
        super().__init__()

    def breathe(self):
        # s189-1-1-3 如果要在方法中调用父类方法，需要使用super.
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()