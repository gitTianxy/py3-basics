# coding=utf-8

import conf.db_config as DBConfig
import threadpool
import threading
from time import sleep
import random
from util.mydbpool import MyDbUtils


def do_query(tbSeq, results):
    try:
        db_conf = DBConfig.local_config
        db_conf.db = 'db_py'
        conn = MyDbUtils.get_connect(db_conf)
        cur = conn.cursor()
        cur.execute("select * from tbl_%s", (tbSeq,))
        random_dur = random.choice(range(0, 10)) / 10.0
        sleep(random_dur)
        mutex.acquire()
        results.extend(cur.fetchall())
        mutex.release()
    except Exception, e:
        print 'error when doing query: ', e.message
    finally:
        cur.close()
        conn.close()


mutex = threading.Lock()
if __name__ == '__main__':
    results = []
    th_pool = threadpool.ThreadPool(10)
    paras = []
    for tbSeq in range(0, 10):
        paras.append((None, {'tbSeq': tbSeq, 'results': results}))
    requests = threadpool.makeRequests(do_query, paras)
    for req in requests:
        th_pool.putRequest(req)
    th_pool.wait()

    results.sort(key=lambda e: e[1])
    for r in results:
        print r
