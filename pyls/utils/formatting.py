from typing import Union 
from datetime import datetime, timezone, timedelta


def format_size(size: Union[int, float], human_readable: bool = False) -> str:
    """
        Format the size in human-readable or standard format.

    Args:
        size (Union[int, float]): File size in bytes.
        human_readable (bool, optional): Whether to format in human-readable format. Defaults to False.

    Returns:
        str: Formatted size string.
    """
    if human_readable:
        if size == 0:
            return "0"

        units = ['', 'K', 'M', 'G', 'T']

        for unit in units:
            if abs(size) < 1024.0:
                return f"{size:.1f}{unit}"
            size /= 1024.0
    else:
        return str(size)

def format_timestamp(timestamp: int) -> str:
    """
        Format the timestamp to a string in the format '%b %d %H:%M'.

    Args:
        timestamp (int): Unix timestamp.

    Returns:
        str: Formatted timestamp string.
    """
    dt = datetime.utcfromtimestamp(timestamp)
    # UTC+5:30 for Asia/Kolkata
    local_dt = dt.replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=5, minutes=30) ))  
    return local_dt.strftime(' %b %d %H:%M')
