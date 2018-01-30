# encoding=utf-8
"""
构造了嵌套类(其中MEntity extends MEntityBase, 并包含InnerEntity),
定义实现其to_json方法
"""
import json
import datetime
from bson import ObjectId
import pprint
from util.date_utils import DateUtils
import abc


class MEntityBase(object):
    """
    mongodb entity base
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, db_entity):
        if db_entity.get("_id") is None:
            self._id = ObjectId()
        else:
            self._id = db_entity.get("_id")

        if db_entity.get("insert_time") is None:
            self.insert_time = datetime.datetime.utcnow()
        else:
            self.insert_time = db_entity.get("insert_time")

        if db_entity.get("update_time") is None:
            self.update_time = datetime.datetime.utcnow()
        else:
            self.update_time = db_entity.get("update_time")

    def pre_persist(self):
        if self.insert_time is None:
            self.insert_time = datetime.datetime.utcnow()
        self.update_time = datetime.datetime.utcnow()

    @abc.abstractmethod
    def to_dic(self):
        pass


class MEntity(MEntityBase):
    """
    entity for test
    """

    def __init__(self, entity):
        super(MEntity, self).__init__(entity)
        self.f1 = entity.get("f1")
        self.f2 = entity.get("f2")
        self.innerEntity = None
        if entity.get("innerEntity") is not None:
            inner_f1 = entity.get("innerEntity").get("inner_f1")
            inner_f2 = entity.get("innerEntity").get("inner_f2")
            self.innerEntity = InnerEntity(inner_f1, inner_f2)

    def to_dic(self):
        self.pre_persist()
        entity_json = {}
        dics = self.__dict__.iteritems()
        for k, v in dics:
            if isinstance(v, InnerEntity):
                entity_json[k] = v.to_dic()
            else:
                entity_json[k] = v
        return entity_json


class InnerEntity:
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

    def to_dic(self):
        entity_json = {}
        dics = self.__dict__.iteritems()
        for k, v in dics:
            entity_json[k] = v
        return entity_json


def json_default(o):
    if type(o) is datetime.datetime:
        return DateUtils.dt2str(o, DateUtils.DATE_PATTERN_LONG)
    elif type(o) is ObjectId:
        return str(o)
    else:
        return o.__dict__


class MyEncoder(json.JSONEncoder):
    """
    encoder for encoding an obj into json-str
    """

    def default(self, o):
        if type(o) is datetime.datetime:
            return DateUtils.dt2str(o, DateUtils.DATE_PATTERN_LONG)
        elif type(o) is ObjectId:
            return str(o)
        else:
            return o.__dict__


if __name__ == "__main__":
    """
    inner_dic = {
        "inner_f1": "inner_f1",
        "inner_f2": "inner_f2"
    }
    dic = {
        "f1": "field1",
        "f2": "field2",
        "innerEntity": inner_dic
    }
    pprint.pprint(MEntity(dic).to_dic())
    # pprint.pprint(json.dumps(obj=MEntity(dic), default=json_default))
    # pprint.pprint(json.dumps(MEntity(dic), cls=MyEncoder))
    """

