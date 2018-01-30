# encoding=utf-8
"""
stack_dump.txt只在程序运行时存在, 退出后即删除
"""
import util.stacktracer as tracer
import time
from multiprocessing import Lock
from multiprocessing.pool import ThreadPool


def tsk(item):
    mutex.acquire()
    print "do task", item['id']
    mutex.release()
    time.sleep(2)
    item['finish'] = True


if __name__ == '__main__':
    mutex = Lock()
    tracer.trace_start('stack_dump.txt', 5, True)
    items = [{
        'id': i,
        'finish': False
    } for i in range(0, 1000)]
    pl = ThreadPool(10)
    pl.map(tsk, items)
    tracer.trace_stop()
