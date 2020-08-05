from multiprocessing import Process
import os


# multiprocessing模块就是跨平台版本的多进程模块

# 子进程要执行的代码
def run_proc(name):
    print('我是子进程运行的任务，我的进程id是：%s，传入的参数是：%s' % (os.getpid(), name))


if __name__ == '__main__':
    print('我是父进程，父进程id： %s.' % os.getpid())  # 获取当前进程(父进程)的id
    p = Process(target=run_proc, args=('刘德华',))  # 开启一个子进程并且制定子进程的任务和传入的参数
    print('子进程即将启动')  # 此时此刻子进程还没有正式运行
    p.start()  # 调用子进程.start()方法正式开启子进程
    p.join()  # 调用子进程.join()方法可以等待子进程结束后继续运行当前的进程(父进程)
    print('子进程运行结束')
