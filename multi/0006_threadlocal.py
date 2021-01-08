# -*- coding: utf-8 -*-
import threading

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>ThreadLocal>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print('一个线程使用自己的局部变量，不会影响其他线程，而全局变量的修改必须加锁')
print()

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
# >>>Hello, Alice (in Thread-A)
# >>>Hello, Bob (in Thread-B)
