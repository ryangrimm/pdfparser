from datetime import datetime
import pytz

def parse_datestring(datestr):
    """coverts date strings in pdf metadata like `u'D:19861200000000'` to
    date objects"""
    date = datetime.strptime(datestr[2:15], '%Y%m%d%H%M%S')
    timezone = pytz.utc
    date = timezone.localize(date)
    return date

__all__ = [parse_datestring]
