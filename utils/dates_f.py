from datetime import datetime

time_based_data = ["day", "week", "month"]


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)


def convert_the_list(list_of_accidents: list):
    for accident in list_of_accidents:
        accident['crash_date']['foll_date'] = parse_date(accident['crash_date']['foll_date'])
    return list_of_accidents
