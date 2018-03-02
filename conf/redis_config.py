# encoding=utf-8
"""
redis setting
"""


class RedisConfig:
    def __init__(self, host, port, password=None):
        self.host = host
        self.port = port
        self.passwd = password


redis_local = RedisConfig(
    host='127.0.0.1',
    port=6379,
)
