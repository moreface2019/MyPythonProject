print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>继承>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
# >>>a is Animal? True
print('a is Dog?', isinstance(a, Dog))
# >>>a is Dog? False
print('a is Cat?', isinstance(a, Cat))
# >>>a is Cat? False

print('d is Animal?', isinstance(d, Animal))
# >>>d is Animal? True
print('d is Dog?', isinstance(d, Dog))
# >>>d is Dog? True
print('d is Cat?', isinstance(d, Cat))
# >>>d is Cat? False

run_twice(c)
# >>>Cat is running...
# >>>Cat is running...
print()

# Java是静态语言，Python是动态语言
print(' 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子')


class Timer(object):
    def run(self):
        print('Start...')


t = Timer()
t.run()
# >>>Start...
