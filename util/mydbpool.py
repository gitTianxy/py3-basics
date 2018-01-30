# coding=utf-8
import pymysql
import pymysql.cursors
import conf.db_config as DBConfig
from DBUtils.PooledDB import PooledDB


class MyDbUtils:
    __pools = {}

    def __init__(self):
        pass

    @staticmethod
    def get_connect(db_config):
        if not isinstance(db_config, DBConfig.DbConfig):
            raise TypeError("db_config should be instance of '../db_config2.DbConfig'")

        pool_key = "%s:%s" % (db_config.type, db_config.db)
        if MyDbUtils.__pools.get(pool_key) is None:
            MyDbUtils.__pools[pool_key] = PooledDB(pymysql, mincached=db_config.mincached,
                                                   maxcached=db_config.maxcached,
                                                   maxconnections=db_config.maxconnections,
                                                   host=db_config.host, user=db_config.user,
                                                   passwd=db_config.passwd,
                                                   port=db_config.port, db=db_config.db)

        return MyDbUtils.__pools[pool_key].connection()
