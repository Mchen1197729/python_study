import os
import random
import time
from multiprocessing import Pool


# 子进程要执行的任务 name代表任务名
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 创建一个容量为4的进程池
    p = Pool(4)
    # 开启了5个任务
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all sub_processes done...')
    # 为什么这里先close()然后再join()呢？？？
    # 因为进程池一共最多执行4个进程 但是现在开启了5个子进程 所以要先等加入进程池的进程都执行完才能再将进程扔进进程池中去执行
    p.close()
    p.join()
    print('All sub_processes done.')
