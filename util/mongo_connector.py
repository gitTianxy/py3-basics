# coding=utf-8
import pymongo
from pymongo import common


class MongoConnector:
    def __init__(self, host, port, opt_dic=None):
        self.host = host
        self.port = port
        self.options = opt_dic

    def __get_uri(self, db, user, pwd):
        uri = "mongodb://%s:%s@%s:%s/%s?" % (user, pwd, self.host, self.port, db)
        if self.options is not None:
            if type(self.options) is not dict:
                raise ValueError("the input 'opt_dic' is not a dict")
            for key, val in self.options.items():
                uri += "%s=%s&" % (key, val)
            uri = uri[:-1]  # remove '&' at tail
        return uri

    def get_db(self, db, user, pwd):
        client = pymongo.MongoClient(self.__get_uri(db, user, pwd))
        return client[db]


local_conn = MongoConnector(
    host="127.0.0.1",
    port=27017,
    opt_dic={
        "connecttimeoutms": common.CONNECT_TIMEOUT,
        "sockettimeoutms": 60000,
        "maxpoolsize": common.MAX_POOL_SIZE,
        "minpoolsize": common.MIN_POOL_SIZE,
        "maxidletimems": 10000,
    }
)
