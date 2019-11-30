import time
import datetime
import pytz


try:
    basestring
except NameError:
    basestring = str


utc_tz = pytz.utc
cn_tz = pytz.timezone('Asia/Shanghai')


def utc_today():
    today_date = datetime.date.today()
    today = cn_tz.localize(datetime.datetime(today_date.year, today_date.month, today_date.day)).astimezone(pytz.utc)
    return today


class Time(object):
    """
    self.timestamp: int, unix 时间戳
    self.datetime: datetime, default_tz 时区下的当地时间
    self.datetime_string: str, default_tz 时区下的当地时间字符串
    self.utc_datetime: datetime, utc 时区的 datetime
    """
    default_format = "%Y-%m-%d %H:%M:%S"
    default_tz = cn_tz

    def __init__(self, t, fmt=None, tz=None):
        if fmt:
            self.default_format = fmt
        if tz:
            self.default_tz = tz

        if isinstance(t, (int, float)):
            if t < 0:
                raise ValueError('init param time except be a utc timestamp')
            self.timestamp = t
            self.utc_datetime = utc_tz.localize(datetime.datetime.utcfromtimestamp(t))
            self.datetime = self.utc_datetime.astimezone(self.default_tz)
            self.datetime_string = self.datetime.strftime(self.default_format)
        elif isinstance(t, basestring):
            self.datetime_string = t
            self.datetime = self.default_tz.localize(datetime.datetime.strptime(t, self.default_format))
            self.utc_datetime = self.datetime.astimezone(utc_tz)
            self.timestamp = int(time.mktime(time.strptime(self.datetime_string, self.default_format)))
        else:
            raise ValueError('init param time except be a utc timestamp or'
                             'a datetime string, got {}'.format(t))
