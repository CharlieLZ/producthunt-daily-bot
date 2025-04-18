import os
import pytz
from datetime import datetime, timezone, timedelta
from typing import Optional

def convert_to_beijing_time(utc_time_str: str, language: str) -> str:
    """
    Convert UTC time string to Beijing time string
    
    Args:
        utc_time_str: UTC time string, format '%Y-%m-%dT%H:%M:%SZ'
        language: language: en/zh
    Returns:
        str: formatted Beijing time string
    """
    try:
        utc_time = datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ')
        beijing_tz = pytz.timezone('Asia/Shanghai')
        beijing_time = utc_time.replace(tzinfo=pytz.utc).astimezone(beijing_tz)
        if language == 'zh':
            return beijing_time.strftime('%Y年%m月%d日 %p%I:%M (北京时间)')
        else:
            return beijing_time.strftime('%Y-%m-%d %p%I:%M (UTC+8 Beijing Time)')
    except Exception as e:
        print(f"Time conversion failed: {utc_time_str}, error: {e}")
        return utc_time_str




def get_yesterday_date() -> str:
    """
    Get yesterday's date string
    
    Returns:
        str: date string in 'YYYY-MM-DD' format
    """
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')

def ensure_directory_exists(directory: str) -> None:
    """
    Ensure the specified directory exists, create if not
    
    Args:
        directory: directory path
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def format_time_duration(seconds: float) -> str:
    """
    Format time duration
    
    Args:
        seconds: number of seconds
    
    Returns:
        str: formatted time string, accurate to 2 decimal places
    """
    return f"{seconds:.2f} seconds"

def get_current_time_str() -> str:
    """
    Get formatted current time string
    
    Returns:
        str: time string in 'YYYY-MM-DD HH:MM:SS' format
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')