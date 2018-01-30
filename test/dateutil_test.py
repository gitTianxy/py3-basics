# coding=utf-8
from util.date_utils import DateUtils

if __name__ == '__main__':
    td = DateUtils.get_this_day()
    print("today. start:%s, end:%s" % (td.get_start_time(), td.get_end_time()))

    print("start time of today. str:%s, ts:%s" % (DateUtils.dt2str(td.get_start_time()), DateUtils.dt2ts(td.get_start_time())))
