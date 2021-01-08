# -*- coding: utf-8 -*-
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>定制类>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    # 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，不会在__getattr__中查找
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    # 只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
print(s)
# >>>Student object (name: Michael)
print(s.name)
# >>>Michael
print(s.score)
# >>>99
print(s.age())
# >>>25
s()
# >>>My name is Michael.
