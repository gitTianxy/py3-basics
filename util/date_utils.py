# coding=utf-8
"""
__title__ date-util
__author__ Kevin Tian
__date__ 2017.7
"""
import datetime, time, calendar


class DateUtils:
    """
    date util for:
    1. transform representations of time
    2. get time-range(start_time, end_time) of a day/week/month
    """
    DATE_PATTERN_SHORT = '%Y-%m-%d'
    DATE_PATTERN_LONG = '%Y-%m-%d %H:%M:%S'

    def __init__(self):
        pass

    @staticmethod
    def str2dt(date_str, pattern=DATE_PATTERN_LONG):
        """
        transform 'date_str' of certain 'pattern' to date_time
        :param date_str:
        :param pattern:
        :return:
        """
        try:
            return datetime.datetime.strptime(date_str, pattern)
        except:
            raise ValueError('error of input date_str or pattern')

    @staticmethod
    def dt2str(date_time, pattern=DATE_PATTERN_LONG):
        """
        transform 'date_time' to a date-string of certain 'pattern'
        :param date_time:
        :param pattern:
        :return:
        """
        if not isinstance(date_time, datetime.datetime):
            print('input type: ', type(date_time))
            raise ValueError("please input datetime")
        return date_time.strftime(pattern)

    @staticmethod
    def dt2ts(date_time):
        """
        transform 'date_time' to its timestamp(time_in_seconds)
        :param date_time:
        :return:
        """
        if not isinstance(date_time, datetime.datetime):
            print('input type: ', type(date_time))
            raise ValueError("please input datetime")
        return time.mktime(date_time.timetuple())

    @staticmethod
    def ts2dt(time_in_seconds):
        """
        transform a timestamp to datetime
        :param time_in_seconds:
        :return:
        """
        try:
            return datetime.datetime.fromtimestamp(time_in_seconds)
        except:
            raise

    @staticmethod
    def get_this_day():
        return DateUtils.get_day(datetime.datetime.now())

    @staticmethod
    def get_this_week():
        return DateUtils.get_week(datetime.datetime.now())

    @staticmethod
    def get_this_month():
        return DateUtils.get_month(datetime.datetime.now())

    @staticmethod
    def get_day(input_time):
        if not isinstance(input_time, datetime.datetime):
            print('input type: ', type(input_time))
            raise ValueError("please input datetime")
        current_ts = time.mktime(input_time.timetuple())
        start_ts = current_ts - input_time.hour * 3600 - input_time.minute * 60 - input_time.second
        end_ts = current_ts + (23 - input_time.hour) * 3600 + (59 - input_time.minute) * 60 + (60 - input_time.second)
        day_start = datetime.datetime.fromtimestamp(start_ts)
        day_end = datetime.datetime.fromtimestamp(end_ts)
        return TimeRange(start_time=day_start, end_time=day_end)

    @staticmethod
    def get_week(input_time):
        if not isinstance(input_time, datetime.datetime):
            print('input type: ', type(input_time))
            raise ValueError("please input datetime")
        input_day = DateUtils.get_day(input_time)
        week_day = input_time.weekday()
        week_start_ts = time.mktime(input_day.get_start_time().timetuple()) - week_day * 24 * 3600
        week_end_ts = time.mktime(input_day.get_end_time().timetuple()) + (6 - week_day) * 24 * 3600
        week_start = datetime.datetime.fromtimestamp(week_start_ts)
        week_end = datetime.datetime.fromtimestamp(week_end_ts)
        return TimeRange(start_time=week_start, end_time=week_end)

    @staticmethod
    def get_month(input_time):
        if not isinstance(input_time, datetime.datetime):
            print('input type: ', type(input_time))
            raise ValueError("please input datetime")
        input_day = DateUtils.get_day(input_time)
        month_range = calendar.monthrange(input_time.year, input_time.month)[1]
        month_start_ts = time.mktime(input_day.get_start_time().timetuple()) - (input_time.day - 1) * 24 * 3600
        month_end_ts = time.mktime(input_day.get_end_time().timetuple()) + (month_range - input_time.day) * 24 * 3600
        month_start = datetime.datetime.fromtimestamp(month_start_ts)
        month_end = datetime.datetime.fromtimestamp(month_end_ts)
        return TimeRange(start_time=month_start, end_time=month_end)


class TimeRange:
    """
    time-range object: include start_time and end_time of a interval
    """

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time
