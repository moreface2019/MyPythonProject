print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>list 列表 & tuple 数组>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# >>>list 列表 & tuple 数组
print("list是用中括号[]，tuple是用小括号()")
# >>>list是用中括号[]，tuple是用小括号()

list = ["Michael", "Bob", "Tracy", ]
print("list data is", list)
# >>>list data is ['Michael', 'Bob', 'Tracy']
list.sort()
print("list after sort is", list)
# >>>list after sort is ['Bob', 'Michael', 'Tracy']

list.append("Kernel")
list.insert(1, "Elsa")
print("list length is", len(list))
# >>>list length is 5
print("list is", list)
# >>>list is ['Bob', 'Elsa', 'Michael', 'Tracy', 'Kernel']
list.pop(1)
print("list is", list)
# >>>list is ['Bob', 'Michael', 'Tracy', 'Kernel']

print("list[0] is", list[0], "list[-1] is", list[-1])
# >>>list[0] is Bob list[-1] is Kernel

list[0] = 123
list[1] = True
list[-1] = ["Kernel", "Elsa"]
print("list data is", list)
# >>>list data is [123, True, 'Tracy', ['Kernel', 'Elsa']]
print("list[-1][-1] is", list[-1][-1])
# >>>list[-1][-1] is Elsa

tuple = ("Michael", "Bob", "Tracy")
print("tuple data is", tuple)
# >>>tuple data is ('Michael', 'Bob', 'Tracy')
print("tuple length is", len(tuple))
# >>>tuple length is 3

tuple = ()
print("tuple data is", tuple)
# >>>tuple data is ()
print("tuple length is", len(tuple))
# >>>tuple length is 0

print("(1)", "is not tuple")
# >>>(1) is not tuple
print("(1,)", "is tuple")
# >>>(1,) is tuple

tuple = ('a', 'b', ['A', 'B'])
tuple[2][0] = 'X'
tuple[2][1] = 'Y'
print("tuple data is", tuple)
# >>>tuple data is ('a', 'b', ['X', 'Y'])
