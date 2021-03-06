# coding=utf-8
"""
# SQLite
SQLite是一种嵌入式数据库，它的数据库就是一个文件。
由于SQLite本身是C写的，而且体积很小，所以经常被集成到各种应用程序中.
Python就内置了SQLite3. 所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
"""

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'sqlite_test.db')
if os.path.isfile(db_file):
    os.remove(db_file)


# 初始数据:
def init_data():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute("insert into user values ('A-001', 'Adam', 95)")
    cursor.execute("insert into user values ('A-002', 'Bart', 62)")
    cursor.execute("insert into user values ('A-003', 'Lisa', 78)")
    cursor.close()
    conn.commit()
    conn.close()


def get_score_in(low, high):
    """
    返回指定分数区间的`(name, score)`，按分数从低到高排序
    :param low:
    :param high:
    :return:
    """
    sql = '''
    select name,score from user
    where
    score>=?
    and
    score<?
    order by score
    '''
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(sql, (low, high))
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return [(col[0], col[1]) for col in res]


if __name__ == '__main__':
    init_data()
    assert get_score_in(80, 96) == [('Adam', 95)]
    assert get_score_in(60, 80) == [('Bart', 62), ('Lisa', 78)]
    assert get_score_in(60, 100) == [('Bart', 62), ('Lisa', 78), ('Adam', 95)]
