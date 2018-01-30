# encoding=utf-8
"""
ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表.
这样，写代码更简单，不用直接操作SQL语句。
"""
from contextlib import closing
from util.mydbpool import MyDbUtils
import conf.db_config_local as DBConfig
from util.date_utils import DateUtils
import datetime
from MySQLdb.cursors import DictCursor


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name, len):
        super(StringField, self).__init__(name, 'varchar(%s)' % len)


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print('Found model: %s' % name)
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        # attrs['__table__'] = name  # 假设表名和类名一致(不可取)
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        print '--- init model'
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            field = v.name
            value = getattr(self, k, None)
            if value is not None:
                fields.append(field)
                params.append('%s')
                args.append(value)
        fields.append('create_time')
        params.append('%s')
        args.append(DateUtils.dt2str(datetime.datetime.now(), DateUtils.DATE_PATTERN_LONG))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
        conn = MyDbUtils.get_connect(DBConfig.local_config)
        with closing(conn) as conn, closing(conn.cursor()) as cur:
            cur.execute(sql, args)
            conn.commit()

    @staticmethod
    def get_by_id(id):
        tbl = User.__table__
        fields = []
        mappings = User.__mappings__.iteritems()
        for k, f in mappings:
            fields.append(f.name)

        sql = "select %s from %s where id=%s" % (','.join(fields), tbl, id)
        conn = MyDbUtils.get_connect(DBConfig.local_config)
        with closing(conn) as conn, closing(conn.cursor(DictCursor)) as cur:
            cur.execute(sql)
            result = cur.fetchone()

        u = User()
        for f in fields:
            u.__setattr__(f, result[f])
        return u


class User(Model):
    __table__ = 'user'
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('name', 20)
    email = StringField('email', 20)
    password = StringField('password', 20)
    crtTime = StringField('create_time', 20)
    updateTime = StringField('update_time', 20)


if __name__ == "__main__":
    '''
    # create
    for name in ['Zhang', 'Wang', 'Li']:
        u = User(name=name, email='%s@orm.org' % name, password='%s-pwd' % name)
        u.save()
    '''
    # retrieve
    u = User.get_by_id(12345)
    print "%s: %s" % (type(u), u)
