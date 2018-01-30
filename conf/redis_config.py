# encoding=utf-8
"""
redis setting
"""


class RedisConfig:
    def __init__(self, host, port):
        self.host = host
        self.port = port


redis_local = RedisConfig(
    host='127.0.0.1',
    port=6379
)