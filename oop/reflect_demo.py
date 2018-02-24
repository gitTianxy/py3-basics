# coding=utf-8
import datetime
import bson
from inspect import signature


class ParantDemo(object):
    def __init__(self):
        self.p_attr_pub = bson.ObjectId()
        self._p_attr_pro = datetime.datetime.utcnow()
        self.__p_attr_pri = "parent-attr-private"

    def pm(self):
        return "parent method"


class SonDemo(ParantDemo):
    def __init__(self):
        super(SonDemo, self).__init__()
        self.s_attr_pub = "son-attr-public"
        self._s_attr_pro = "son-attr-proteced"
        self.__s_attr_pri = "son-attr-private"

    def sm(self):
        return "son method"


def call_methods(obj):
    for a in dir_itr(obj):
        m = getattr(obj, a)
        if callable(m) and len(signature(m).parameters) == 0:
            print(f"call method '{a}': {m()}")


def call_attrs(obj):
    for a in dir_itr(obj):
        if not callable(getattr(obj, a)):
            print(f"{a}:{getattr(obj, a)}")


def dir_itr(obj):
    return [a for a in dir(obj) if not a.startswith('__')]


def dict_itr(obj):
    return obj.__dict__.items()


if __name__ == "__main__":
    son = SonDemo()
    print("---reflect by 'getattr()'")
    call_attrs(son)
    call_methods(son)
    print("---reflect by 'dict'")
    dict_res = dict_itr(son)
    for k, v in dict_res:
        print("%s: %s" % (k, v))