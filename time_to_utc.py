from datetime import datetime

def convert_timestamp_to_utc(timestamp: str) -> float | int:
    date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')

    return date.timestamp()