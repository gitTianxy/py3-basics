# coding=utf-8

'''
TEST:
1. Code would be executed on 'import'
2. 'main' module is the one on 'RUN'
'''

msg = 'hello, this is main1'

print msg


def print_msg():
    print msg


if __name__ == '__main__':
    print 'this is __main__ in main1'
