import time
import os
import random

from multiprocessing import Process, Pool


def sub_target(a):
    print('sub_process %s is running pid: %s' % (a, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('sub_process %s costs %0.2f s' % (a, (end - start)))


if __name__ == '__main__':
    print('main_process is running...')
    p = Pool(4)
    for x in range(10):
        p.apply_async(sub_target, ('进程%s' % x,))
    print('waiting for all sub_process done...')
    p.close()
    p.join()
    print('main_process ends')
