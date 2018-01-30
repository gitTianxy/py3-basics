# coding=utf-8
import MySQLdb
from contextlib import closing
import conf.db_config as DBConfig

conn = MySQLdb.connect(
    host=DBConfig.local_config.host,
    port=DBConfig.local_config.port,
    user=DBConfig.local_config.user,
    passwd=DBConfig.local_config.passwd,
    db='db_py',
)

insert_tpl = "insert into tbl_%s values(%s,%s,%s)"
create_tbl_tpl = '''
    CREATE TABLE tbl_%s (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` INT NOT NULL,
        `value` VARCHAR(20) NOT NULL,
        PRIMARY KEY (`id`));
'''
create_tbl_all = '''
    CREATE TABLE tbl_all (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` INT NOT NULL,
        `value` VARCHAR(20) NOT NULL,
        PRIMARY KEY (`id`));
'''
drop_tbl_tpl = "drop table if exists tbl_%s"
queryall_sql = "select * from tbl_all"
TBL_NUM = 10


def init():
    # create table_all
    with closing(conn.cursor()) as cur:
        cur.execute(create_tbl_all)
        conn.commit()
    # init data
    with closing(conn.cursor()) as cur:
        for i in range(0, 10000):
            try:
                sql = insert_tpl % ('all', i, i, i)
                cur.execute(sql)
            except Exception, e:
                pass
        conn.commit()
    # create table_xxx
    for i in range(0, TBL_NUM):
        create_tbl(i)


def create_tbl(tbSeq):
    with closing(conn.cursor()) as cur:
        cur.execute(drop_tbl_tpl, (tbSeq,))
        conn.commit()
        cur.execute(create_tbl_tpl, (tbSeq,))
        conn.commit()


def insert_data(tbSeq, values):
    with closing(conn.cursor()) as cur:
        vals = (tbSeq,) + values
        cur.execute(insert_tpl, vals)
        conn.commit()


def sharding_tbl():
    with closing(conn.cursor()) as cur:
        cur.execute(queryall_sql)
        results = cur.fetchall()
        for item in results:
            tbSeq = item[1] % TBL_NUM
            values = (item[0], item[1], item[2])
            insert_data(tbSeq, values)


if __name__ == '__main__':
    # init()
    sharding_tbl()
