# encoding=utf-8
"""
json data reaa/write
---
"""
import json
import datetime
import requests

jstr = '''
{
    "data": {
        "status": -1,
        "accountId": 109,
        "storage": "swift",
        "md5": "efbcba252e5b23695c6fbbc1cd631681",
        "fid": 445792,
        "imgs": "1.jpg,2.jpg,3.jpg,4.jpg,5.jpg,",
        "cid": 150646379,
        "file_size": 2399217093,
        "extend": {},
        "insert_time": 1407045075000,
        "last_update_time": 1516163682156,
        "features": {
            "feature_bt256": "bcb04a1536ff9b573d9730a60ae29f9b",
            "feature_xunlei_gcid": "2399217093_1A627C9BE5F2C6AA7CA1AAA2A0CD89F19A14DF2D",
            "feature_bt64": "ab55c22589e94205883f15771a0005af",
            "feature_ed2k": "2399217093_c57531069647c4ea7759f6a7f15efe59",
            "feature_pplive": "2399217093_7ce3a098fedd08abb065c4ab4b136bec046ee771",
            "feature_bt512": "892b10db1c670f0c831c27e00c5c61ac",
            "feature_xunlei_cid": "2399217093_c327c0f2717ceba6f7af8d2bc9945527e8a2ce73",
            "feature_bt1024": "727ad9917dcbc91731462c5729a8c3ec",
            "feature_bt32": "7f775585ce8afaf5101466089506ac02",
            "feature_shooter": "adc952382111cd13a02f28a0cdcab2ad;61f7e36bbba6f398c3fa975b646adaf8;844fe8f44a09751d75766d80583ffd37;69170a1808ed9666ad4a23381a050523",
            "feature_bt128": "9b3c3f0c452a741f4689f75e7b11a508"
        },
        "default_img": "1.jpg",
        "filecps": {
            "private_cloud": {
                "status": -1,
                "fromcp": "private_cloud",
                "fid": 445792,
                "cid": 150646379,
                "insert_time": 1407045075000,
                "last_update_time": 1516163682000
            }
        },
        "download_url": null
    },
    "err": 0
}
'''

jfile = '../data/fileinfo_{fid}.json'


def parse_str():
    print '---parse json str to dict'
    fdeadline = datetime.datetime.strptime('2016-06-01', '%Y-%m-%d')
    res = json.loads(jstr)
    if res['err'] != 0:
        print 'err happens'
        return
    finfo = res['data']
    fid = finfo['fid']
    last_update_time = datetime.datetime.fromtimestamp(finfo['last_update_time']/1000)
    fromcps = finfo['filecps'].values()
    print 'fid:', fid
    print "last_update_time(%s) before deadline(%s): %s" % (last_update_time, fdeadline, (last_update_time < fdeadline))
    print "fromcp is 'private_cloud':", (len(fromcps) == 1 and fromcps[0]['fromcp'] == 'private_cloud')
    return finfo


def load_file(jpath):
    print '---load json file'
    with open(jpath) as f:
        print 'json file content:', json.load(f)


def dict_2_jstr(obj):
    '''
    json.dumps(obj)
    '''
    print '---convert dict 2 json str'
    print json.dumps(obj)


def dict_2_jsonf(obj, fpath):
    '''
    json.dump(obj,file)
    '''
    print '---write dict 2 json file'
    with open(fpath, 'w') as f:
        json.dump(obj, f)


def read_json_by_http(fid):
    print '---read json from http request'
    res = None
    try:
        url = 'http://ppc.pptvyun.com/fsvc/private/3/file/{fid}'.replace('{fid}', str(fid))
        res = requests.get(url, headers={
            'Accept': 'application/json'
        })
        if res.status_code == requests.codes.ok:
            print json.loads(res.text)['data']
        else:
            raise RuntimeError(
                "get fileinfo err. fid:%s, status:%s, reason:%s" % (fid, res.status_code, res.reason))
    except:
        raise
    finally:
        if res:
            res.close()


if __name__ == '__main__':
    finfo = parse_str()
    # fpath = jfile.replace('{fid}', str(finfo['fid']))
    # dict_2_jsonf(obj=finfo, fpath=fpath)
    # load_file(fpath)
    # dict_2_jstr(finfo)
    read_json_by_http(finfo['fid'])
