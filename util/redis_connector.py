# coding=utf8
"""
module for redis connection
"""
import redis


class RedisConnector:
    def __init__(self):
        pass

    @staticmethod
    def get_conn(host, port, passwd=None):
        return redis.Redis(host=host, port=port, password=passwd)


class DBConf:
    def __init__(self, host, port, passwd=None):
        self.host = host
        self.port = port
        self.passwd = passwd


local_conf = DBConf(host='127.0.0.1', port=6379)
