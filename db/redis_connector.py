# encoding=utf-8
"""
module for redis connection
"""
import redis


class RedisConnector:
    def __init__(self):
        pass

    @staticmethod
    def get_conn(host, port):
        return redis.Redis(host=host, port=port)


if __name__ == "__main__":
    conn = RedisConnector.get_conn('127.0.0.1', 6379)
    pipe = conn.pipeline()
    pipe.hget("htian", "age")
    result = pipe.execute()
    print result
