# -*- coding: utf-8 -*-
import os
from multiprocessing import Process

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>多进程 multiprocessing>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print('Process (%s) start...' % os.getpid())
print()

print('Unix/Linux操作系统提供了一个fork()系统调用，Windows没有fork调用')
print('fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回')
print('子进程永远返回0，而父进程返回子进程的ID。下面的代码在Windows上无法运行')

# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
print()

print('multiprocessing模块提供了一个Process类来代表一个进程对象')


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # >>>Parent process 10196.
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # >>>Child process will start.
    p.start()
    # >>>Run child process test (10196)...
    p.join()
    # >>>Child process end.
    print('Child process end.')
    print('创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。')
    print('join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。')
    print()
