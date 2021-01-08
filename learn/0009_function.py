# -*- coding: utf-8 -*-
import functools

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>函数式编程>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
x = abs(-2)
print('x is', x)
# >>>x is 2

f = abs
print('f is', f)
# >>>f is <built-in function abs>
print('f(-10) is', f(-10))
# >>>f(-10) is 10

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>高阶函数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def add(x, y, f):
    return f(x) + f(y)


def minus(x):
    return -x


print(add(5, -6, abs))
# >>>11
print(add(5, -6, minus))
# >>>1

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>map/reduce>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

from functools import reduce


def square(x):
    return x * x


def add(x, y):
    return x + y


print('map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回')
r = map(square, [1, 2, 3, 4])
print('r is', r)
# >>>r is <map object at 0x0000025161686670>
print(list(r))
# >>>[1, 4, 9, 16]

print('reduce把结果继续和序列的下一个元素做累积计算')
print(reduce(add, [1, 2, 3, 4]))
# >>>10
r = map(square, [1, 2, 3, 4])
print(reduce(add, r))
# >>>30

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>filter>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


print('filter把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素')
r = list(filter(is_odd, range(20)))
print('r is', r)
# >>>r is [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

r = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print('r is', r)
# >>>r is ['A', 'B', 'C']

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>sorted>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
l = [36, 5, -12, 9, -21]
print(sorted(l))
# >>>[-21, -12, 5, 9, 36]
print(sorted(l, key=abs))
# >>>[5, 9, -12, -21, 36]
print(sorted(l, key=abs, reverse=True))
# >>>[36, -21, -12, 9, 5]

l = ['bob', 'about', 'Zoo', 'Credit']
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(l))
# >>>['Credit', 'Zoo', 'about', 'bob']
print(sorted(l, key=str.lower))
# >>>['about', 'bob', 'Credit', 'Zoo']
print(sorted(l, reverse=True))
# >>>['bob', 'about', 'Zoo', 'Credit']
print(sorted(l, key=str.lower, reverse=True))
# >>>['Zoo', 'Credit', 'bob', 'about']

l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
from operator import itemgetter

print(sorted(l, key=itemgetter(0)))
# >>>[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
print(sorted(l, key=itemgetter(1), reverse=True))
# >>>[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>返回函数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print('f is', f)
# >>>f is <function lazy_sum.<locals>.sum at 0x0000020B9E55D940>
print('f() is', f())
# >>>f() is 25

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>匿名函数 lambda>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('关键字lambda表示匿名函数，冒号前面的x表示函数参数')
# 匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果
f = lambda x: x * x
print(f(6))


# >>>36

def build(x, y):
    return lambda: x * x + y * y


f = build(3, 4)
print(f())
# >>>25
print(build(6, 8)())
# >>>100

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>装饰器 Decorator>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('函数对象有一个__name__属性，可以拿到函数的名字')


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s() ... ' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("2020-06-19")


now()
# >>>call now() ...
# >>>2020-06-19

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>偏函数 functools.partial>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
print(int('aaaf', base=16))
# >>>43695

# base=2，表示参数是2进制数，通过int方法转化成10进制
int2 = functools.partial(int, base=2)
print(int2('10101010'))
# >>>170
print(int2('11'))
# >>>3

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
# >>>10
