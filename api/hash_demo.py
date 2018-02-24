# encoding=utf-8

import hashlib
import base64
import hmac


def calc_base64(url_param):
    """
    Base64是一种用64个字符来表示任意二进制数据的方法(bytes->str)。
    ---
    由于标准的Base64编码后可能出现字符+,/,=，在URL中就不能直接作为参数，
    所以又有一种"url safe"的base64编码，其实就是把字符+,/分别变成-和_, 并去掉=
    """

    code = base64.b64encode(url_param.encode('utf8'))
    print("base64 encoded:", code)
    decode = base64.b64decode(code)
    print("base64 decoded:", decode)
    uscode = base64.urlsafe_b64encode(url_param.encode('utf8'))
    print("url-safe encoded:", uscode)
    usdecode = base64.urlsafe_b64decode(uscode)
    print("url-safe decoded:", usdecode)


def hmac_MD5(key, fpath):
    """
    1. Hmac算法
    Keyed-Hashing for Message Authentication。
    它在计算哈希的过程中，把key混入计算过程中。
    2. 安全性
    hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。
    3. 通用性
    Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。
    采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
    4. hmac vs 普通hash算法
    使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。
    需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
    """
    with open(fpath, 'rb') as f:
        h = hmac.new(key.encode('utf8'), f.read(), digestmod='MD5')
    print(h.hexdigest())


def calc_Sha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash


def calc_MD5(filepath):
    with open(filepath, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash


if __name__ == "__main__":
    fpath = '../data/sqlite_test.db'
    print(calc_MD5(fpath))
    print(calc_Sha1(fpath))
    params = 'https://www.liaoxuefeng.com/wiki?q1=1&q2=2'
    calc_base64(params)
    hmac_MD5('salt', fpath)
