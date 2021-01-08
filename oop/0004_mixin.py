# -*- coding: utf-8 -*-
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>mixin 多重继承>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


class Animal(object):
    pass


# 大类:哺乳，鸟类
class Mammal(Animal):
    def waa(self):
        print('Mammal...')


class Bird(Animal):
    pass


# 功能：跑，飞
class RunnableMixIn(Animal):
    def run(self):
        print('Running...')

    def waa(self):
        print('RunnableMixIn...')


class FlyableMixIn(Animal):
    def fly(self):
        print('Flying...')

    def waa(self):
        print('FlyableMixIn...')


# 各种动物:狗，蝙蝠
class Dog(RunnableMixIn, Mammal):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


# 同时存在waa方法，靠前的class生效
d = Dog()
d.run()
# >>>Running...
d.waa()
# >>>RunnableMixIn...

b = Bat()
b.fly()
# >>>Flying...
b.waa()
# >>>Mammal...
