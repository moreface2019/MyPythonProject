print("条件判断>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("if elif else")

age = 20
print("Your age is", age)
# >>>Your age is 20
if age >= 18:
    print("You are adult")
    # >>>You are adult
    age = 8
elif age >= 6:
    print("You are teenager")
    age = 4
else:
    print("You are kid")
print("Your age is", age)
# >>>Your age is 8

x = 'abc'
if x:
    print("x是非零数值、非空字符串、非空list")
# >>>x是非零数值、非空字符串、非空list
else:
    print("x是零数值、空字符串、空list")

birth = input("birth: ")
# string 转 int 类型
birth = int(birth)
if (birth < 2000):
    print("00前")
else:
    print("00后")
