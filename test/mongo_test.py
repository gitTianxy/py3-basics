# coding=utf-8
"""
MongoDB 测试
"""
from util.mongo_connector import local_conn

if __name__ == '__main__':
    mongo = local_conn.get_db('springboot', 'kevin', '1234')
    res = mongo['user'].find({
        'name': 'kevin'
    })
    for u in res:
        print("_id:%s, name:%s, age:%s" % (u['_id'], u['name'], u['age']))
