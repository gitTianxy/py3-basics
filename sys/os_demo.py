# encoding=utf-8
import os

print 'current work directory:', os.getcwd()

print "file path relative to 'cwd':", __file__

fpath = os.path.realpath(__file__)
print "file pull path:", fpath

print os.path.split(fpath)

s = 'hello/hello/hello/hello'
print s[:s.rindex('/')]
