from datetime import datetime
from pytz import timezone

DATETIME_FORMAT = '%m/%d/%Y %H:%M:%S'

def convert_datetime(value, format):
  try:
    given_datetime = datetime.strptime(value, format)
    given_datetime_local_tz = given_datetime.astimezone(timezone('US/Eastern'))
    return given_datetime_local_tz.strftime(DATETIME_FORMAT)
  except:
    return ''
