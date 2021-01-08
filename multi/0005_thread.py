# -*- coding: utf-8 -*-4
import threading
import time

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>多线程 threading>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    # >>>thread LoopThread is running...
    n = 0
    while n < 3:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        # >>>thread LoopThread >>> 1
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
    # >>>thread LoopThread ended.


print('thread %s is running...' % threading.current_thread().name)
# >>>thread MainThread is running...
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
# >>>thread MainThread ended.

print()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>锁 Lock>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n + n
    balance = balance - n


def run_thread(n):
    # 先要获取锁:
    lock.acquire()
    try:
        change_it(n)
    finally:
        lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
print('balance is', balance)
t1.start()
t2.start()
print('balance is', balance)
t1.join()
t2.join()
print('balance is', balance)
