# encoding=utf-8
"""
CONTENTS:
    1. basic process demo: os fork process
    2. multiprocess demo
    3. a multiprocess-multithread demo
    4. a processpool-threadpool demo
"""
import multiprocessing
import os
import time
from multiprocessing.pool import ThreadPool
import threading
import random


class ProcessBaseDemo:
    """
    os.fork():
        1. 执行过程--one fork(), two returns:
            1) 将os.fork()开始的代码行复制两份,一份放入主进程(当前进程), 一份放入子进程
            2) 开启主进程并执行代码, 其中os.fork()返回子进程pid
            3) 开启子进程并执行代码, 其中os.fork()返回0
        2. only works on Unix/Linux
    NOTE:
        父进程调用sleep(), 则将运行权交给子进程, 直到:
            1) sleep()结束重新夺回运行权
            2) 子进程(结束)把运行权返回;
        子进程中一旦调用sleep(), 立即把运行权返回给父进程, 子进程后台异步执行(主/父进程不等待其结束)
    """

    def __init__(self):
        print('basic process demo ---------------')
        self.flag = None
        pid = os.fork()
        print('os.fork() return pid', pid)
        if pid == 0:
            print("'CHILD' process runs...pid=", os.getpid())
            # time.sleep(3)
            # print("'CHILD' process stop")
        else:
            print("'PARENT' process runs...pid=", os.getpid())
            # time.sleep(1)
            # time.sleep(5)
            # print("'PARENT process stop")


class MultiProcessDemo:
    """
    multiprocessing.Process
    ---
    1. create process
    2. start process
    3. wait process finish
    """

    def __init__(self):
        print('multi-process demo -------------')
        print('Parent process %s.' % os.getpid())
        cps = []
        for idx in range(0, 10):
            cps.append(multiprocessing.Process(target=self.run_proc, name=('p%s' % idx), args=(idx,)))
        for cp in cps:
            print('%s process START' % cp.name)
            cp.start()
        for cp in cps:
            cp.join()
            print('%s process END' % cp.name)

    def run_proc(self, index):
        print("%s process is running...index=%s, pid=%s" % (multiprocessing.current_process().name, index, os.getpid()))


class ProducerConsumerDemo:
    """
    3 bases:
        1. a shared queue: multiprocessing.Queue
        2. producer-process: multiprocessing.Process
        3. consumer-process: multiprocessing.Process
    """

    def __init__(self):
        print('producer-consumer processes demo -------------')
        # 父进程创建Queue，并传给各个子进程：
        q = multiprocessing.Queue()
        pw = multiprocessing.Process(target=self.write, args=(q,))
        pr = multiprocessing.Process(target=self.read, args=(q,))
        self.wend = False
        # 启动子进程pw，写入:
        pw.start()
        # 启动子进程pr，读取:
        pr.start()
        # 等待pw结束:
        pw.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:
        pr.terminate()

    def write(self, q):
        print("'PRODUCER' process start. pid:", os.getpid())
        for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            q.put(value)
            time.sleep(1)

    def read(self, q):
        print("'CONSUMER' process start. pid:", os.getpid())
        while True:
            value = q.get(True)
            print('Get %s from queue.' % value)
        print("unreachable code")


class MultiProcessMultiThreadDemo:
    global mutex

    def __init__(self):
        print('multi-process multi-thread demo -------------')
        processes = []
        # tasks = ['tsk-%s' % i for i in range(0, 10)]
        for idx in range(0, 5):
            processes.append(multiprocessing.Process(target=self.run_proc, name=('process-%s' % idx), args=()))
        for process in processes:
            mutex.acquire()
            print('%s START' % process.name)
            mutex.release()
            process.start()
        for process in processes:
            process.join()
            mutex.acquire()
            print('%s FINISH' % process.name)
            mutex.release()

    def run_proc(self):
        pname = multiprocessing.current_process().name
        pid = os.getpid()
        tasks = ['tsk_p%s_%s' % (pid, i) for i in range(0, 10)]
        mutex.acquire()
        print('process %s (%s) is running...' % (pname, pid))
        mutex.release()
        ThreadPool().map(func=self.run_thread, iterable=tasks)

    def run_thread(self, task):
        mutex.acquire()
        print('Run thread %s, do %s' % (threading.currentThread().name, task))
        mutex.release()


class ProcessPoolDemo:
    """
    NOTE: apply_async()里的func需要是pickleable的, 根据python的语法定义,此function需要定义在top level of the module,
        即不能包裹在其他function或者class内部
    """

    def __init__(self):
        print('process-pool demo -------------')
        print('Parent process %s.' % os.getpid())
        p = multiprocessing.Pool()
        for i in range(10):
            p.apply_async(long_time_task, args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s spends %0.2f seconds.' % (name, (end - start)))


mutex = threading.Lock()
if __name__ == "__main__":
    # ProcessBaseDemo()
    process_base_demo = multiprocessing.Process(target=ProcessBaseDemo, name='process-base')
    process_base_demo.start()
    process_base_demo.join()
    # MultiProcessDemo()
    multi_process_demo = multiprocessing.Process(target=MultiProcessDemo, name='multi-process')
    multi_process_demo.start()
    multi_process_demo.join()
    # ProducerConsumerDemo()
    readwrite_process_demo = multiprocessing.Process(target=ProducerConsumerDemo, name='readwrite-processes')
    readwrite_process_demo.start()
    readwrite_process_demo.join()
    # MultiProcessMultiThreadDemo()
    multiprocess_multithread_demo = multiprocessing.Process(target=MultiProcessMultiThreadDemo,
                                                            name='multiprocess-multithread')
    multiprocess_multithread_demo.start()
    multiprocess_multithread_demo.join()
    # ProcessPoolDemo()
    process_pool_demo = multiprocessing.Process(target=ProcessPoolDemo, name='process-pool')
    process_pool_demo.start()
    process_pool_demo.join()
