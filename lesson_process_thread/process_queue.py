from multiprocessing import Queue, Process
import time, random


def write(q):
    for x in ['A', 'B', 'C', 'D']:
        print('put %s into queue' % x)
        q.put(x)
        time.sleep(random.random())


def read(q):
    while True:
        print('read %s from queue' % q.get(True))


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
