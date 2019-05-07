from datetime import datetime
from pytz import timezone

DATETIME_FORMAT = '%m/%d/%Y %H:%M:%S'


def format_datetime(datetime_value: datetime) -> str:
    try:
        return datetime_value.strftime(DATETIME_FORMAT)
    except Exception:
        return ''


def convert_datetime_to_local_timezone(value: str, datetime_format: str) -> datetime:
    try:
        given_datetime = datetime.strptime(value, datetime_format)
        return given_datetime.astimezone(timezone('US/Eastern'))
    except Exception:
        return None
