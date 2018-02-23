# encoding=utf-8

import hashlib


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
    file_path = "/Users/kevin/Workspace/python/pptv/GZTV_512000_20171125_26723853_0.mp4"
    print(calc_MD5(file_path))
    print(calc_Sha1(file_path))
