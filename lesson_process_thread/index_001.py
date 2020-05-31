import multiprocessing
import os
import time
from multiprocessing import Process

print(multiprocessing.cpu_count())


# 开启多进程(两个进程之间没有通信)
def target_a(a, b, c):
    # a就是args[0] b就是args[1] c就是args[2]
    for x in range(30):
        print(x, a, b, os.getpid(), c)
        time.sleep(0.1)


def target_b(a, b, c):
    # a就是args[0] b就是args[1] c就是args[2]
    for x in range(30):
        print(x, a, b, os.getpid(), c)
        time.sleep(0.2)


if __name__ == '__main__':
    print('main_process is running pid: %s' % os.getpid())
    pa = Process(target=target_a, args=('process_a', 'aaaaaaa', 'cccccccc'))
    pb = Process(target=target_b, args=('process_b', 'bbbbbbb', 'cccccccc'))
    pa.start()
    pb.start()
    pa.join()
    pb.join()
    pa.close()
    pb.close()
