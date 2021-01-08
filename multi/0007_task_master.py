# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>分布式进程 QueueManager>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print('服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务')
print()

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 自定义函数re_task_queue
def re_task_queue():
    global task_queue
    return task_queue


# 自定义函数re_result_queue
def re_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=re_task_queue)
    QueueManager.register('get_result_queue', callable=re_result_queue)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        task.put(n)
        time.sleep(3)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # 关闭:
    manager.shutdown()
    print('master exit.')
