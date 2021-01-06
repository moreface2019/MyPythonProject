print("Hello Python", "测试中文是否乱码")
# >>>Hello Python 测试中文是否乱码

# str to bytes
b = str.encode('Hello')
print(b)
# >>>b'Hello'

# bytes to str
s = bytes.decode(b'world')
print(s)
# >>>world

a = 'abc'
b = a
a = 'xyz'
print('a=', a, "and", 'b=', b)
# >>>a= xyz and b= abc

# 用r''表示字符串不转义
print(r'\\\t\\', "is ", '\\\t\\', )
# >>>\\\t\\ is  \	\

# 用'''XXX'''的格式表示多行内容
print('''line1
line2
line3''')
# >>>line1
# >>>line2
# >>>line3

# / 除法计算结果是浮点数，// 称为地板除，结果仍然是整数，% 称为余数运算
print('10/3=', 10 / 3, "and 10//3=", 10 // 3, 'and 10%3=', 10 % 3)
# >>>10/3= 3.3333333333333335 and 10//3= 3 and 10%3= 1

r = (85 - 72) * 100 / 72
print("Hi, %s, 恭喜你战胜了%.2f%%的选手" % ('walker', r))
# >>>Hi, walker, 恭喜你战胜了18.06%的选手
print("Hello, {0:s}, 成绩提升了{1:.2f}%".format("小明", r))
# >>>Hello, 小明, 成绩提升了18.06%

a = "abca"
b = a.replace("a", "A")
print(a)
# >>>abca
print(b)
# >>>AbcA

print("len('abc') is", len('abc'))
# >>>len('abc') is 3
print("len('中文') is", len('中文'))
# >>>len('中文') is 2
# b表示字节数
print("len(b'ABC') is", len(b'ABC'))
# >>>len(b'ABC') is 3
print("'中文'.encode('utf-8') is", len('中文'.encode('utf-8')))
# >>>'中文'.encode('utf-8') is 6

# 输入wangtao
name = input("enter your name: ")
print("your name is", name)
# >>>your name is wangtao
s
