# encoding=utf-8
"""
es operations with the package 'elasticsearch'
----------------------------------------------
ISSUES:
    1. CRUD index
    2. save document
    3. get document
    4. search with condition
"""
from util.date_utils import DateUtils
from elasticsearch import Elasticsearch
from time import sleep
import pprint


def init_es(hosts, timeout=10):
    return Elasticsearch(hosts=hosts, timeout=timeout)


def create_idx(idx, settings, mappings):
    """
    Create index with `settings` and `mappings`
    :param idx:
    :param settings:
    :param mappings:
    :return:
    """
    global es
    body = {}
    if settings:
        body['settings'] = settings
    if mappings:
        body['mappings'] = mappings
    es.indices.create(index=idx, body=body, ignore=400)


def get_idx(idx):
    global es
    try:
        return es.indices.get(index=idx)
    except Exception, e:
        print e
        return None


def delete_idx(idx):
    global es
    es.indices.delete(index=idx)


def save_document(idx, doc_type, doc_id, doc):
    """
    Adds or updates a typed JSON document in a specific index, making it searchable.
    :param idx:
    :param doc_type:
    :param doc_id:
    :param doc:
    :return:
    """
    global es
    es.index(index=idx, doc_type=doc_type, id=doc_id, body=doc)


def get_document(idx, doc_type, doc_id):
    global es
    return es.get(index=idx, doc_type=doc_type, id=doc_id)


def get_documents(idx, doc_type, ids):
    global es
    return es.mget(body={'ids': ids}, index=idx, doc_type=doc_type)


def del_document(idx, type, id):
    global es
    es.delete(index=idx, doc_type=type, id=id)


def update_document(idx, type, id, doc):
    global es
    es.update(index=idx, doc_type=type, id=id, body={"doc": doc})


def search(idx, doc_type, query, sort=[], start=0, size=10):
    global es
    res = {}
    res['start'] = start
    res['page_size'] = size

    res['hits'] = \
        es.search(index=idx, doc_type=doc_type, body={'query': query, 'sort': sort, 'from': start, 'size': size})[
            'hits'][
            'hits']
    res['count'] = len(res['hits'])
    return res


es = None
if __name__ == '__main__':
    # preparation
    es = init_es(hosts=[{'host': '127.0.0.1', 'port': 9200}])
    idx = 'my_index'
    if get_idx(idx):
        delete_idx(idx)
    # create index
    create_idx(idx=idx, settings=None, mappings=None)
    # save document
    doc_type = 'people'
    for id in range(0, 50):
        doc = {"name": ('name%s' % id), "age": 10 + id,
               "birthday": DateUtils.str2dt('2000-01-01', DateUtils.DATE_PATTERN_SHORT)}
        save_document(idx=idx, doc_type=doc_type, doc_id=id, doc=doc)
    # get document
    print '-----------------------------'
    docs = get_documents(idx=idx, doc_type=doc_type, ids=[i for i in range(0, 50)])['docs']
    for doc in docs:
        print doc
    # update document
    doc_new = {"name": 'name0_NEW', "age": 10,
               "birthday": DateUtils.str2dt('2017-01-01', DateUtils.DATE_PATTERN_SHORT)}
    update_document(idx=idx, type=doc_type, id=0, doc=doc_new)
    # del document
    del_document(idx=idx, type=doc_type, id=1)
    # search -- there is a time-delay before search launch
    print '-----------------------------'
    sleep(5)
    es_query = {
        "bool": {
            "must": [
                {
                    "terms": {
                        "_id": [str(i) for i in range(0, 20)]
                    }
                },
                {
                    "range": {
                        "age": {"lte": "20"}
                    }
                }
            ],
            "must_not": [],
            "should": []
        }
    }
    pprint.pprint(search(idx=idx, doc_type=doc_type, query=es_query, size=50))
