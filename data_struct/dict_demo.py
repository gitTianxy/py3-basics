# coding=utf-8
"""
1. dict复制
"""

# data
dict_demo = dict(a=1, b=2, c=3)

dict_new = dict(dict_demo)
dict_new['d'] = 4

# display
print '-----------'
for k, v in dict_demo.iteritems():
    print '%s: %s' % (k, v)
print '-----------'
for k, v in dict_new.iteritems():
    print '%s: %s' % (k, v)

# keys
for k in dict_demo.keys():
    print 'key:', k

# values
for v in dict_demo.values():
    print 'value:', v
