from datetime import datetime

def parse_datestring(datestr):
    """coverts date strings in pdf metadata like `u'D:19861200000000'` to
    date objects"""
    return datetime.strptime(datestr[2:15], '%Y%m%d%H%M%S')

__all__ = [parse_datestring]
