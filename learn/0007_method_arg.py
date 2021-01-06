print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>位置参数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


r = power(5, 4)
print('power(5, 4) is', r)
# >>>power(5, 4) is 625

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>默认参数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def my_print(name, gender, age=6, city='Shenyang'):
    print('name:', name, 'gender:', gender, 'age:', age, 'city:', city)


my_print('Elsa', "F", 4)
# >>>name: Elsa gender: F age: 4 city: Shenyang
my_print("Kernel", "M", city='Shanghai')
# >>>name: Kernel gender: M age: 6 city: Shanghai

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>可变参数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


r = calc(1, 2, 3, 4)
print('calc(1, 2, 3, 4) is', r)
# >>>calc(1, 2, 3, 4) is 10
nums = range(5)
r = calc(*nums)
print('calc(*nums) is', r)
# >>>calc(*nums) is 10

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>关键字参数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'extra:', kw)


person('Walker', '36')
# >>>name: Walker age: 36 extra: {}
person('Walker', '36', city='Shenyang', gender='M')
# >>>name: Walker age: 36 extra: {'city': 'Shenyang', 'gender': 'M'}
extra = {'city': 'Shanghai', 'job': 'Engineer'}
person('Jack', 24, **extra)
# >>>name: Jack age: 24 extra: {'city': 'Shanghai', 'job': 'Engineer'}

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>命名关键字参数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 只接收city和gender作为关键字参数
def person(name, age, *, city, gender):
    return name, age, city, gender


r = person('Walker', '36', city='Shenyang', gender='M')
print(r)


# >>>('Walker', '36', 'Shenyang', 'M')

def person(name, age, *args, city="Shanghai", gender="M"):
    sum_extra = calc(*args)
    return name, age, sum_extra, city, gender


nums = [1, 2, 3, 4]
r = person("Elsa", 8, *nums, gender="F")
print(r)
# >>>('Elsa', 8, 10, 'Shanghai', 'F')

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>参数组合>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 参数组合定义的顺序必须是：位置参数、默认参数、可变参数、命名关键字参数和关键字参数
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
def f1(a, b, c=0, *args, **kw):
    print('f1', 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'extra =', kw)


f1(1, 2, 3, 'a', 'b', x=99)
# >>>f1 a = 1 b = 2 c = 3 args = ('a', 'b') extra = {'x': 99}
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


# >>>f1 a = 1 b = 2 c = 3 args = (4,) extra = {'d': 99, 'x': '#'}

def f2(a, b, c=0, *, d, **kw):
    print('f2', 'a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(1, 2, d=99, ext=None)
# >>>f2 a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# >>>f2 a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
