# coding=utf8
from urllib import request
import ssl


def https_download(url, fpath):
    req = request.Request(url)
    res = request.urlopen(req, context=ssl._create_unverified_context())
    with open(fpath, 'wb') as f:
        f.write(res.read())


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
    fpath = 'Auto.csv'
    https_download(url, fpath)
