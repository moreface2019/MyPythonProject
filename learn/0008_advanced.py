import os
from collections.abc import Iterable, Iterator

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>切片>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print("L[0:3] is", L[0:3])
# >>>L[0:3] is ['Michael', 'Sarah', 'Tracy']
print("L[:3] is", L[:3])
# >>>L[:3] is ['Michael', 'Sarah', 'Tracy']
print("L[2:4] is", L[2:4])
# >>>L[2:4] is ['Tracy', 'Bob']
print("L[2:2] is", L[2:2])
# >>>L[2:2] is []
print("L[3:] is", L[3:])
# >>>L[3:] is ['Bob', 'Jack']
print("L[3] is", L[3])
# >>>L[3] is Bob
print("L[4:5] is", L[4:5])
# >>>L[4:5] is ['Jack']
print()

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print("L[-2:] is", L[-2:])
# >>>L[-2:] is ['Bob', 'Jack']
print("L[-2:0]is", L[-2:0])
# >>>L[-2:0]is []
print("L[-2:-1]is", L[-2:-1])
# >>>L[-2:-1]is ['Bob']
print("L[-2:-4] is", L[-2:-4])
# >>>L[-2:-4] is []
print("L[-1:] is", L[-1:])
# >>>L[-1:] is ['Jack']
print("L[-1] is", L[-1])
# >>>L[-1] is Jack
print()

l = list(range(100))
print(l[:10:2])  # 前10个数，每两个取一个
# >>>[0, 2, 4, 6, 8]
print(l[::5])  # 所有数，每5个取一个
# >>>[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
print()

t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[2:7:2])
# >>>(2, 4, 6)
str = 'abcdefghijklmn'
print(str[::3])
# >>>adgjm
print()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>迭代 Iterable>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, value)
for ch in "ABC":
    print(ch)
print()

print(isinstance('ABC', Iterable))
# >>>True
print(isinstance([1, 2, 3], Iterable))  # List
# >>>True
print(isinstance((1, 2, 3), Iterable))  # Tuple
# >>>True
print(isinstance({'a', 'b', 'c'}, Iterable))  # dict
# >>>True
print(isinstance(123, Iterable))
# >>>False
print()

# enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate([1, 2, 3, ]):
    print(i, value)
# >>> 0 1 # >>> 1 2 # >>> 2 3
for x, y, z in [(1, 1, 1), (2, 4, 8), (3, 9, 27)]:
    print(x, y, z)
# >>> 1 1 1 # >>> 2 4 8 # >>> 3 9 27

for t in [(1, 1, 1), (2, 4, 8), (3, 9, 27)]:
    print(t)
# >>> (1, 1, 1) # >>> (2, 4, 8) # >>> (3, 9, 27)
print()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>列表生成式>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
list = list(range(1, 11))
print(list)
# >>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list = [x * x for x in range(1, 11)]
print(list)
# >>>[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

t = (x * x for x in range(1, 11))
print('t is', t)
for d in t:
    pass
# >>>t is <generator object <genexpr> at 0x000001478DBB0AC0>
list = [x * x for x in range(1, 11) if x % 2 == 0]
print(list)
# >>>[4, 16, 36, 64, 100]

list = [m + n for m in 'ABC' for n in 'XYZ']
print(list)
# >>>['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

list = [m + n for m in [1, 2, 3] for n in [1, 2, 3]]
print(list)
# >>>[2, 3, 4, 3, 4, 5, 4, 5, 6]

list = [d for d in os.listdir('..')]
print(list)
# >>>['MyAndroidProject', 'MyJ2EEProject', 'MyPythonProject', 'Shenyang']

d = {'x': 'A', 'y': 'B', 'z': 'C'}
list = [k + ":" + v for k, v in d.items()]
print(list)
# >>>['x:A', 'y:B', 'z:C']

list = [s.lower() for s in list]
print(list)
# >>>['x:a', 'y:b', 'z:c']

# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
list = [x for x in range(1, 11) if x % 2 == 0]
print(list)
# >>>[2, 4, 6, 8, 10]

list = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(list)
# >>>[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
print()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>生成器 generator>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
g = (x * x for x in range(11))
r = 0
for n in g:
    r = r + n
print('r is', r)


# >>>r is 385

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Over'


f = fib(6)
r = 0
for n in f:
    r = r + n
print('r is', r)
# >>>r is 20

print()
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>迭代器 Iterator>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。 可迭代对象
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。  迭代器
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，把list、dict、str等Iterable变成Iterator可以使用iter()函数

print(isinstance([], Iterable))
# >>>True
print(isinstance([], Iterator))
# >>>False
print(isinstance(iter([]), Iterator))
# >>>True
