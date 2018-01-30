# encoding=utf-8
"""
INCLUDES:
    1. thread_local
    2. threading.Thread
    3. self-defined runnable class
"""
import threading
from time import sleep
import random
from datetime import datetime


class ThreadLocalDemo:
    """
    ThreadLocal的作用: 用于定义'在线程间相互独立但类型相同的资源'
    用法:
        1. 定义一个ThreadLocal类型的共享变量
        2. 在子线程中把资源作为属性塞到共享变量中
        3. 此后各线程即可通过threadlocal变量独立访问各自的资源
    """
    global mutex

    def __init__(self):
        print 'thread local demo ---------------------'
        self.local_school = threading.local()
        t1 = threading.Thread(target=self.process_thread, args=('Alice',), name='Thread-A')
        t2 = threading.Thread(target=self.process_thread, args=('Bob',), name='Thread-B')
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def process_student(self):
        # 获取当前线程关联的student:
        std = self.local_school.student
        mutex.acquire()
        print('Hello, %s (in %s)' % (std, threading.current_thread().name))
        mutex.release()

    def process_thread(self, name):
        # 绑定ThreadLocal的student:
        self.local_school.student = name
        sleep(random.random())
        self.process_student()


class ThreadDemo:
    """
    NOTE:
        python里的多线程只能在'单核'上执行!因为解释器CPython的进程有一个GIL锁(Global Interpreter Lock)机制:
    所有线程在获取时间片之前都要竞争GIL,所以某一时刻只有一个线程在执行,当然也就只能用到一个核.
        要实现多核任务, 可以通过多进程来实现
    """
    global mutex

    def __init__(self):
        print 'thread demo ---------------------'
        # init
        threads = []
        t1 = threading.Thread(target=self.music, args=('kevin-music', 5,))
        threads.append(t1)
        t2 = threading.Thread(target=self.movie, args=('kevin-movie', 10,))
        threads.append(t2)
        # start threads
        for t in threads:
            t.start()
        # main-thread wait
        for t in threads:
            t.join()

    def music(self, name, dur):
        mutex.acquire()
        print 'START listen music'
        mutex.release()
        start = datetime.now()
        while True:
            if (datetime.now() - start).seconds > dur:
                mutex.acquire()
                print 'STOP listen music'
                mutex.release()
                break
            mutex.acquire()
            print 'listen', name
            mutex.release()
            sleep(1)

    def movie(self, name, dur):
        print 'START watch movie '
        start = datetime.now()
        while True:
            if (datetime.now() - start).seconds > dur:
                mutex.acquire()
                print 'STOP watch movie'
                mutex.release()
                break
            mutex.acquire()
            print 'watch', name
            mutex.release()
            sleep(1)


class MyThreadDemo:
    """
    self-defined runnable class
    """
    global mutex

    def __init__(self):
        print 'self-defined thread demo ---------------------'
        # init
        threads = []
        t1 = self.MyThread("listen music", 5)
        threads.append(t1)
        t2 = self.MyThread("watch movie", 10)
        threads.append(t2)
        # start threads
        for t in threads:
            t.start()
        # main-thread wait
        for t in threads:
            t.join()

    class MyThread(threading.Thread):
        """
        a runnable class
        """
        def __init__(self, operation, dur):
            threading.Thread.__init__(self)
            self.operation = operation
            self.dur = dur

        def run(self):
            mutex.acquire()
            print 'START ', self.operation
            mutex.release()
            start = datetime.now()
            while True:
                if (datetime.now() - start).seconds > self.dur:
                    mutex.acquire()
                    print 'STOP ', self.operation
                    mutex.release()
                    break
                mutex.acquire()
                print self.operation
                mutex.release()
                sleep(1)


mutex = threading.Lock()
if __name__ == "__main__":
    ThreadLocalDemo()
    ThreadDemo()
    MyThreadDemo()
