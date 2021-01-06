import math


def my_print(str):
    print("my_print:", str)
    return "over"


# 空函数,什么事也不做
def do_nothing():
    pass  # 用来作为占位符,让代码能运行起来


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>函数>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

r = max(1, 3, 8, abs(-10))
print('r is', r)
# >>>r is 10
print(str(float("12.34")))
# >>>12.34
print(int(12.34))
# >>>12
print(bool(int(12.34)))
# >>>True

# 把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-2))
# >>>2

res = my_print("hello, pyhton")
# >>>my_print: hello, pyhton
print(res)
# >>>over

age = 20
if age >= 18:
    pass  # 缺少了pass，代码运行就会有语法错误

do_nothing()

print('# 返回多个值')


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print('%.2f' % x, y)
# >>>151.96 70.0
r = move(100, 100, 60, math.pi / 6)
print(r)
# >>>(151.96152422706632, 70.0)

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>递归>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


f = fact(5)
print('fact(5) is', f)
# >>>fact(5) is 120

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>尾递归>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
# 求和是sum，求积是product
def fact(num, product):
    if num == 1:
        return product
    return fact(num - 1, num * product)


f = fact(5, 1)
print('fact(5, 1) is', f)
# >>>fact(5, 1) is 120
