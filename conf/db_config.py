# coding=utf-8
TYPE_LOCAL = "local"


class DbConfig:
    """
    db config obj
    """

    def __init__(self, type, host, port, user, passwd, mincached, maxcached, maxconnections, db):
        self.type = type
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.mincached = mincached
        self.maxcached = maxcached
        self.maxconnections = maxconnections
        self.db = db

    def set_db(self, db):
        self.db = db


# local
local_config = DbConfig(
    type=TYPE_LOCAL,
    host="127.0.0.1",
    user="kevin",
    passwd="1234",
    port=3306,
    mincached=3,
    maxcached=100,
    maxconnections=10,
    db='pptv_publiccloud'
)
