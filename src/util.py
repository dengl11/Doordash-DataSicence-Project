import json
from datetime import datetime, timedelta
from calendar import timegm


def load_prediction_todo(k = -1):
    """
    Kwargs:
        k: how many entries to load, -1 to load all

    Return: 
    """
    if k < 0: k = float('inf')
    with open("./data/data_to_predict.json", 'r') as f:
        ans = []
        for l in f.readlines():
            if k <= 0: break
            ans.append(json.loads(l))
            k -= 1
        return ans

def parse_utc_timestamp(timestamp : str):
    """
    Args:
        timestamp: string format of utc time
                   e.g. "2015-02-25 02:22:30"

    Return: a datetime object
    """
    utc_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    return utc_time

def diff_timestamps(t1 : str, t2 : str):
    """
    Args:
        t1: 
        t2: 

    Return: 
    """
    t1, t2 = parse_utc_timestamp(t1), parse_utc_timestamp(t2)
    return (t2 - t1).total_seconds()

def add_timestamp_by_seconds(t0, seconds_elapsed):
    """
    Args:
        t0: 
        seconds_elapsed: 

    Return: 
    """
    t = parse_utc_timestamp(t0) + timedelta(seconds = seconds_elapsed)
    return t.strftime("%Y-%m-%d %H:%M:%S")
