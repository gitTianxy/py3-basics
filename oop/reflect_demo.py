# coding=utf-8
import datetime
import bson
import inspect


class ParantDemo(object):
    def __init__(self):
        self.p_attr_pub = bson.ObjectId()
        self._p_attr_pro = datetime.datetime.utcnow()
        self.__p_attr_pri = "parent-attr-private"


class SonDemo(ParantDemo):
    def __init__(self):
        super(SonDemo, self).__init__()
        self.s_attr_pub = "son-attr-public"
        self._s_attr_pro = "son-attr-proteced"
        self.__s_attr_pri = "son-attr-private"


def dir_itr(obj):
    return [a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj, a))]


def dict_itr(obj):
    return obj.__dict__.iteritems()


if __name__ == "__main__":
    son = SonDemo()
    dir_res = dir_itr(son)
    for k in dir_res:
        v = getattr(son, k)
        print("%s: %s" % (k, v))
    print('-----------------------')
    dict_res = dict_itr(son)
    for k, v in dict_res:
        print("%s: %s" % (k, v))