# encoding=utf-8
"""
pymongo aggregate demo
"""
from util.mongo_connector import MongoConnector


def get_tbl_orders():
    """
    order table resc by to-del-fid count
    ---
    db.getCollection('del_outdate_fid').aggregate([
        {$match: {isdel: 0}},
        {$group:{_id:'$tbl_idx', count:{$sum: 1}}},
        {$sort:{'count':-1}}
    ])
    :return:
    """
    conn = MongoConnector(host="127.0.0.1", port=27017)
    db = conn.get_db(db="pptv", user="kevin", pwd="1234")
    cur = db['del_outdate_fid'].aggregate([
        {'$match': {'isdel': 0}},
        {'$group': {'_id': '$tbl_idx', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}
    ])
    return [item['_id'] for item in list(cur)]

if __name__ == '__main__':
    print get_tbl_orders()
