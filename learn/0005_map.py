# -*- coding: utf-8 -*-
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>集合>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("dict 字典 & set 去重集合")
print("dict和set使用大括号{}")

d = {"1": "kernel", 2: "Elsa"}
print(d)
# >>>{'1': 'kernel', 2: 'Elsa'}
d["1"] = 100
print(d["1"])
# >>>100
print(d[2])
# >>>Elsa
d.pop("1")
print(d)
# >>>{2: 'Elsa'}
print("1" in d)
# >>>False
print(2 in d)
# >>>True
print(d.get("1"))
# >>>None
print(d.get("1", "default"))
# >>>default

print()
s = set([1, 3, 4, 5, 1, 2, 2, 2, 3, 3, 4])
print(s)
# >>>{1, 2, 3, 4, 5}
s = {1, 2, 2, 4, '66'}
print(s)
# >>>{1, 2, 4, '66'}
s.add("3")
s.remove(4)
print(s)
# >>>{1, 2, '3', '66'}
s.pop()
print(s)
# >>>{2, '3', '66'}

s1 = set([1, 2, 3])
s2 = set([1, 3, 4])
print(s1 & s2)
# >>>{1, 3}
print(s1 | s2)
# >>>{1, 2, 3, 4}
