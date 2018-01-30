# encoding=utf-8
import abc
import datetime
from bson import ObjectId
import pprint


class MEntityBase:
    """
    mongodb entity base
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, db_entity):
        self._id = db_entity.get("_id")
        self.insert_time = db_entity.get("insert_time")
        self.update_time = db_entity.get("update_time")

    def pre_persist(self):
        if self._id is None:
            self._id = ObjectId()
            self.insert_time = datetime.datetime.utcnow()
        self.update_time = datetime.datetime.utcnow()

    def display(self):
        pprint.pprint(self.to_dic(), indent=4, width=1)

    @abc.abstractmethod
    def to_dic(self):
        pass


class MaoBase:
    """
    ===============mongo-access-object base================
    build-in-methods:
        1a. save: 'insert' or 'update'
        1b. insert: insert entity into db
        1c. update: update entity in db
        2. get: retrieve by _id
        3. delete: remove by _id
        4. get_all: retrieve all entities in db
        5. count_all: count all entities in db
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, db, collect_name):
        self.db = db
        self.collect = collect_name

    def save(self, entity):
        """
        save entity 2 db
        :param entity:
        :return:
        """
        old_entity = None
        if getattr(entity, "_id") is not None:
            old_entity = self.get(getattr(entity, "_id"))
        if old_entity is None:
            self.insert(entity)
        else:
            self.update(entity)

    def get(self, _id):
        """
        get entity by '_id'
        :param _id:
        :return:
        """
        db_entity = self.db[self.collect].find_one({
            "_id": ObjectId(_id)
        })
        return self._convert_2_entity(db_entity)

    def get_all(self):
        """
        get all entity of the collection
        :return:
        """
        return [self._convert_2_entity(e) for e in self.db[self.collect].find()]

    def count_all(self):
        """
        count all entity in db
        :return:
        """
        return self.db[self.collect].count()

    def delete(self, _id):
        self.db[self.collect].delete_one({
            "_id": ObjectId(_id)
        })

    def insert(self, entity):
        """
        insert entity into db
        :param entity:
        :return:
        """
        if getattr(entity, "_id") is not None:
            raise ValueError("_id is not null")
        entity.pre_persist()
        self.db[self.collect].insert_one(entity.to_dic())

    def update(self, entity):
        """
        update db entity
        :param entity:
        :return:
        """
        if getattr(entity, "_id") is None:
            raise ValueError("_id is null")
        entity.pre_persist()
        dic_4_update = entity.to_dic()
        dic_4_update.pop("_id", None)
        self.db[self.collect].update({
            "_id": getattr(entity, "_id")
        }, {
            "$set": dic_4_update
        })

    def query(self, skp=0, lmt=5, **kwargs):
        """
        :param skp: skip
        :param lmt: limit
        :param kwargs: other query conditions
        :return:
        """
        return [self._convert_2_entity(e) for e in self.db[self.collect].find(kwargs).skip(skp).limit(lmt)]

    @abc.abstractmethod
    def _convert_2_entity(self, db_dict):
        pass
