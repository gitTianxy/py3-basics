# coding=utf-8
import time
import datetime

# str 2 datetime
start = datetime.datetime.strptime('2017-01-01','%Y-%m-%d')
print 'start-day: ', start

# datetime 2 str
print start.strftime('%Y-%m-%d')

# datetime 2 ts
ts = time.mktime(start.timetuple())

# ts 2 datetime
print 'next-day: ', datetime.datetime.fromtimestamp(ts + 24*3600)

# time comparision
compt = datetime.datetime.strptime('2018-01-17', '%Y-%m-%d')
now = datetime.datetime.now()
print '%s after %s: %s' % (now, compt, now > compt)
print '%s before %s: %s' % (now, compt, now < compt)
