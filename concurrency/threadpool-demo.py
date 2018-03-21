# coding=utf-8
"""
threadpool module demo
---
1. threadpool.ThreadPool
2. threadpool.makeRequests
3. pool.putRequest(req)
4. pool.wait()
"""
from time import sleep
import threading
import threadpool
from datetime import datetime


class MyThread(threading.Thread):
    __inner_prop = "class inner prop"

    def __init__(self, operation, dur):
        threading.Thread.__init__(self)
        self.operation = operation
        self.dur = dur

    def run(self):
        mutex.acquire()
        print('START ', self.operation)
        mutex.release()
        start = datetime.now()
        while True:
            if (datetime.now() - start).seconds > self.dur:
                return self.operation
            mutex.acquire()
            print(self.operation)
            mutex.release()
            sleep(1)

    @staticmethod
    def cb_func(request, name):
        mutex.acquire()
        print(MyThread.__inner_prop)
        if request.exception:
            print('%s is Failed!!!' % name)
        else:
            print('%s is FINISH!!!' % name)
        mutex.release()


def do_work(name, dur):
    start = datetime.now()
    while True:
        if (datetime.now() - start).seconds > dur:
            return name
        mutex.acquire()
        print('do ', name)
        mutex.release()
        sleep(1)


def callback_fn(request, name):
    mutex.acquire()
    if request.exception:
        print('%s is Failed!!!' % name)
    else:
        print('%s is FINISH!!!' % name)
    mutex.release()


def call_method_demo():
    print('------------- call method demo ----------------')
    works = [(None, {'name': 'listen music', 'dur': 5}), (None, {'name': 'watch TV', 'dur': 3})]
    pool = threadpool.ThreadPool(5)
    requests = threadpool.makeRequests(do_work, works, callback_fn)
    for req in requests:
        pool.putRequest(req)
    pool.wait()


def call_class_demo():
    print('-------------- call class-method demo ----------------')
    thread1 = MyThread('listen music', 5)
    thread2 = MyThread('watch TV', 3)
    para = [thread1, thread2]
    pool = threadpool.ThreadPool(2)
    requests = threadpool.makeRequests(MyThread.run, para, MyThread.cb_func)
    for req in requests:
        pool.putRequest(req)
    pool.wait()


mutex = threading.Lock()
if __name__ == '__main__':
    call_method_demo()
    call_class_demo()
