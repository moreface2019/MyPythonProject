# -*- coding: utf-8 -*-
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>循环>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("for & while")

names = ["Michael", "Bob", "Tracy"]
for name in names:
    print(name)
# >>>Michael
# >>>Bob
# >>>Tracy

print('list(range(5, 10)) is', list(range(5, 10)))
# >>>list(range(5, 10)) is [5, 6, 7, 8, 9]
print(range(10))
# >>>range(0, 10)

sum = 0
for x in range(20):
    sum = sum + x
print('sum(range(20))=', sum)
# >>>sum(range(20))= 4950

sum = 0
n = 0
while (sum < 1000):
    if (n >= 20):
        break
    sum = sum + n
    n = n + 1
print("sum is", sum, "n is", n)
# >>>sum is 190 n is 20

n = 0
while n < 5:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
# >>>1
# >>>3
# >>>5
