# encoding=utf-8
"""
CONTENTS:
    1. basic use of process
    2. a multiprocess-multithread demo
    3. a processpool-threadpool demo
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
        1. 执行过程:
            1) 将os.fork()开始的代码行复制两份,一份放入主进程(当前进程), 一份放入子进程
            2) 开启主进程并执行代码, 其中os.fork()返回子进程pid
            3) 开启子进程并执行代码, 其中os.fork()返回0
        2. only works on Unix/Linux
    NOTE: 子进程中一旦调用sleep(), 由于没有其他守护线程所以整个子进程停止--运行权从新交由父进程
    """

    def __init__(self):
        print 'process base demo ---------------'
        self.flag = None
        pid = os.fork()
        print 'os.fork() return pid', pid
        if pid == 0:
            self.flag = 'CHILD'
            self.child_proc()
        else:
            self.flag = 'PARENT'
            self.parent_proc()

    def parent_proc(self):
        print 'Run %s process...pid=%s' % (self.flag, os.getpid())

    def child_proc(self):
        print 'Run %s process...pid=%s' % (self.flag, os.getpid())


class MultiProcessDemo:
    def __init__(self):
        print 'multi-process demo -------------'
        print('Parent process %s.' % os.getpid())
        cps = []
        for idx in range(0, 5):
            cps.append(multiprocessing.Process(target=self.run_proc, name=('cp%s' % idx), args=(idx,)))
        for cp in cps:
            print '%s process will START.' % cp.name
            cp.start()
        for cp in cps:
            cp.join()
            print '%s process has END.' % cp.name

    def run_proc(self, index):
        print 'Run %s process...index=%s, pid=%s' % (multiprocessing.current_process().name, index, os.getpid())


class ReadWriteProcessDemo:
    """
    3 bases:
        1. a shared queue
        2. wirte-process
        3. read-process
    """

    def __init__(self):
        print 'read-write processes demo -------------'
        # 父进程创建Queue，并传给各个子进程：
        q = multiprocessing.Queue()
        pw = multiprocessing.Process(target=self.write, args=(q,))
        pr = multiprocessing.Process(target=self.read, args=(q,))
        # 启动子进程pw，写入:
        pw.start()
        # 启动子进程pr，读取:
        pr.start()
        # 等待pw结束:
        pw.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:
        pr.terminate()

    def write(self, q):
        print('Process to write: %s' % os.getpid())
        for value in ['A', 'B', 'C']:
            print('Put %s to queue...' % value)
            q.put(value)
            time.sleep(1)

    def read(self, q):
        print('Process to read: %s' % os.getpid())
        while True:
            value = q.get(True)
            print('Get %s from queue.' % value)


class MultiProcessMultiThreadDemo:
    global mutex

    def __init__(self):
        print 'multi-process multi-thread demo -------------'
        processes = []
        tasks = ['tsk-%s' % i for i in range(0, 10)]
        for idx in range(0, 5):
            processes.append(multiprocessing.Process(target=self.run_proc, name=('process-%s' % idx), args=(tasks,)))
        for process in processes:
            mutex.acquire()
            print '%s START.' % process.name
            mutex.release()
            process.start()
        for process in processes:
            process.join()
            mutex.acquire()
            print '%s FINISH.' % process.name
            mutex.release()

    def run_proc(self, taskes):
        mutex.acquire()
        print('Run process %s (%s)...' % (multiprocessing.current_process().name, os.getpid()))
        mutex.release()
        ThreadPool().map(func=self.run_thread, iterable=taskes)

    def run_thread(self, task):
        mutex.acquire()
        print 'Run thread %s, do %s' % (threading.currentThread().name, task)
        mutex.release()


class ProcessPoolDemo:
    """
    NOTE: apply_async()里的func需要是pickleable的, 根据python的语法定义,此function需要定义在top level of the module,
        即不能包裹在其他function或者class内部
    """

    def __init__(self):
        print 'process-pool demo -------------'
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
    # ReadWriteProcessDemo()
    readwrite_process_demo = multiprocessing.Process(target=ReadWriteProcessDemo, name='readwrite-processes')
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
