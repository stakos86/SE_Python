from datetime import datetime

FORMATS = ['%Y-%m-%d', '%Y/%m/%d', '%Y.%m.%d']


def is_date_by_format(date, date_format):
    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False


def is_date(date):
    for date_format in FORMATS:
        if is_date_by_format(date, date_format):
            return True
    return False
