from datetime import datetime
from pytz import timezone

DATETIME_FORMAT = '%m/%d/%Y %H:%M:%S'


def convert_datetime(value: str, datetime_format: str) -> str:
  try:
    given_datetime_local_tz = convert_datetime_to_local_timezone(value, datetime_format)
    return given_datetime_local_tz.strftime(DATETIME_FORMAT)
  except:
    return ''

def convert_datetime_to_local_timezone(value: str, datetime_format: str) -> datetime:
  try:
    given_datetime = datetime.strptime(value, datetime_format)
    return given_datetime.astimezone(timezone('US/Eastern'))
  except:
    return None
