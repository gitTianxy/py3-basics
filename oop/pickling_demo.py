# coding=utf8
"""
序列化(pickling)
在程序运行的过程中，所有的变量都是在内存中, 但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
1. dump 2 bytes
2. dump into file

反序列化(unpickling)
把变量内容从序列化的对象重新读到内存里称为反序列化.
1. load from bytes
2. load from file-like object
"""
import pickle


def dump2bytes(content):
    print(f"---dump {content} to bytes")
    return pickle.dumps(content)


def dump2file(content, fpath):
    print(f"---dump {content} to {fpath}")
    with open(fpath, 'wb') as f:
        pickle.dump(content, f)


def loadbytes(content):
    print("---load bytes", content)
    return pickle.loads(content)


def loadfile(fpath):
    print("---load file", fpath)
    with open(fpath, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    obj = dict(name='Bob', age=20, score=88)
    dumps = dump2bytes(obj)
    print(dumps)
    bres = loadbytes(dumps)
    print(bres)
    fpath = './dump.txt'
    dump2file(obj, fpath)
    fres = loadfile(fpath)
    print(fres)
