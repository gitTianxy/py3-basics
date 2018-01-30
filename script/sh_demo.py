# encoding=utf-8
"""
在python中执行shell脚本
-------------------------------------
1. os.system
2. os.popen
3. commands
"""
import os
import commands


def os_system_demo(cmd):
    """
    该方法在调用完shell脚本后，返回一个16位的二进制数，低位为杀死所调用脚本的信号号码，高位为脚本的退出状态码。
    返回的结果都是0（使用位运算向右位移8位得到的结果就是高位值），代表代码正常退出。
    我们如果需要的到脚本执行后返回的状态码，可以使用位运算得到。
    :param cmd:
    :return:
    """
    return os.system(cmd) >> 8


def os_popen_demo(cmd):
    """
    这种调用方法是通过管道的方式来实现的，函数返回一个file-like的对象，里面的内容是脚本输出的内容
    :param cmd:
    :return:
    """
    return os.popen(cmd)


@DeprecationWarning
def cmd_filestatus(file):
    """
    return status
    :param file:
    :return:
    """
    return commands.getstatus(file)


def cmd_output(cmd):
    """
    return output
    :param cmd:
    :return:
    """
    return commands.getoutput(cmd)


def cmd_status_output(cmd):
    """
    return (status, output) tuple
    :param cmd:
    :return:
    """
    (status, output) = commands.getstatusoutput(cmd)
    return (status >> 8, output)


if __name__ == '__main__':
    name = raw_input('please input name:')
    cmd_file = '../data/hello.sh'
    hello_cmd = cmd_file + ' ' + name
    print 'status:', os_system_demo('ls')
    print 'status:', os_system_demo(hello_cmd)
    print 'return:', os_popen_demo('ls').read()
    print 'return:', os_popen_demo(hello_cmd).read()
    print 'return:', os_popen_demo('cat ' + cmd_file).read()
    print 'output:', cmd_output(hello_cmd)
    print 'status:%s, output:%s' % cmd_status_output(hello_cmd)
