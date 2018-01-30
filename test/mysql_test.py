# coding=utf-8
"""
test mysql db
"""
import conf.db_config as DBConfig
from contextlib import closing
import threadpool
import threading
from util.mydbpool import MyDbUtils

'''
for testing db connection
'''

mutex = threading.Lock()


def query_demo(sql, db_config):
    global mutex
    conn = MyDbUtils.get_connect(db_config)
    with closing(conn.cursor()) as cur:
        cur.execute(sql)
        mutex.acquire()
        print("OK")
        mutex.release()


def job_demo():
    pool = threadpool.ThreadPool(5)
    works = []
    sql = "SELECT 1"
    for i in range(0, 10):
        work = (None, {'sql': sql, 'db_config': DBConfig.local_config})
        works.append(work)
    requests = threadpool.makeRequests(query_demo, works)
    for req in requests:
        pool.putRequest(req)
    pool.wait()
    print("-------------------\nFINISH")


if __name__ == "__main__":
    job_demo()
