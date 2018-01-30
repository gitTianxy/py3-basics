# coding=utf-8
"""
multiprocessing.pool.ThreadPool demo
----------------------------
NOTE:
    1. 线程函数只能有一个参数: 下方'process','thr_tsk'只能带一个参数
    2. 在multiprocessing中用其Lock, 在threading中用对应的Lock
TIPS:
    1. 不宜在子线程函数中使用global变量
    2. 在前一个pool.map()结束之前不会开启后一个pool.map()
    3. 线程异常情况下'线程池线程等待'可用'pool.close()+pool.join()'的方案
    3a. 当一个pool.map()中的某些任务抛异常终止后, 会立即(在pool中其余线程结束之前)执行pool.map()之后的代码;
    当然, 如果被try-except包裹则立即执行except中及finally中的代码. 所以需要在except中添加pl.close() pl.join()的等待语句
    3b. 当一个pool里有线程发生异常, 则等pool中已分配的所有线程执行完就终止此轮pool.map任务, 而不会让任务队列中的任务走完.
    比如有100个任务塞进10线程的线程池, 当某一轮次pool中有线程发生异常, 则等其余9个任务走完, 就终止pool的所有线程;
    而正常情况下会用这10个线程把100个任务跑完.
"""
from time import sleep
from multiprocessing.pool import ThreadPool
from multiprocessing import Lock
import random


def tsk_a(idx):
    global rd
    global mutex
    if random.random()*100 > 99:
        raise RuntimeError("err happens in 'task A'. round:%s, index:%s" % (rd, idx))
    mutex.acquire()
    print "do 'task A'. round:%s, index:%s" % (rd, idx)
    mutex.release()
    sleep(10)


def tsk_b(idx):
    global rd
    global mutex
    if random.random() > 0.6:
        raise RuntimeError("err happens in 'task B'. round:%s, index:%s" % (rd, idx))
    mutex.acquire()
    print "do 'task B'. round:%s, index:%s" % (rd, idx)
    mutex.release()
    sleep(2)


if __name__ == '__main__':
    thr_num = 20
    mutex = Lock()
    pl = ThreadPool(thr_num)
    err_num = 0
    rd = 0
    while True:
        try:
            mutex.acquire()
            print "---NEW round start. round:", rd
            mutex.release()
            pl.map(tsk_a, range(0, 50))
            pl.map(tsk_b, range(0, 20))
        except Exception, ex:
            err_num += 1
            mutex.acquire()
            print "error:%s, error num:%s" % (ex, err_num)
            mutex.release()
            pl.close()
            pl.join()
            pl = ThreadPool(thr_num)
        finally:
            mutex.acquire()
            print "round %s FINISH." % rd
            mutex.release()
            rd += 1

        if err_num > 5:
            mutex.acquire()
            print 'err happened %s times. slp 10secs...' % err_num
            sleep(10)
            err_num = 0
            mutex.release()
