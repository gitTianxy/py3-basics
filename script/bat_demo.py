# encoding=utf-8
"""
python 执行 .bat 脚本
"""
import os
from subprocess import *


def os_system_demo(file):
    status = os.system(file) >> 8
    if status == 0:
        print 'succ'
    else:
        print 'fail'


def os_popen_demo(file):
    return os.popen(file)


def subprocess_popen_demo(file):
    p = Popen(file, shell=True, stdout=PIPE)
    print 'out:%s, err:%s' % p.communicate()
    if p.returncode == 0:
        print 'succ'
    else:
        print 'fail'


if __name__ == '__main__':
    bat_file = 'D:/pyprojects/py-basics/data/hello.bat'
    os_system_demo(bat_file)
    print os_popen_demo(bat_file).read()
    subprocess_popen_demo(bat_file)
