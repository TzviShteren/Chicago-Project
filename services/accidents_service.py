from services.logger import *
from repository.accidents_repository import *
from utils.dates_f import *
import datetime


def get_sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence, request_info):
    try:
        result = sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence)
        log(request_info)
        return result
    except Exception as e:
        log_error(e)
        return {}


def Check_the_week_number_is_correct(number):
    return not number < 1 or number > 53


def filter_the_specific_week(beat_of_occurrence, number):
    get_all_accidents = get_all_accidents_by_beat(beat_of_occurrence)
    convert_to_data = convert_the_list(get_all_accidents)
    # Reference taken from: https://stackoverflow.com/questions/2600775/how-to-get-week-number-in-python
    filter_result = list(filter(lambda x: x['crash_date']['foll_date'].isocalendar()[1] == number, convert_to_data))
    return filter_result


def get_sum_of_accidents_by_beat_end_date(unit, number, beat_of_occurrence, request_info):
    try:
        if unit == 'day':
            result = sum_of_accidents_by_beat_end_day(beat_of_occurrence, number)
        elif unit == 'week' and Check_the_week_number_is_correct(number):
            filter_result = filter_the_specific_week(beat_of_occurrence, number)
            result = len(filter_result)
        elif unit == 'month':
            result = sum_of_accidents_by_beat_end_month(beat_of_occurrence, number)
        else:
            return {}
        log(request_info)
        return result
    except Exception as e:
        log_error(e)
        return {}


def get_sum_of_contributory_cause_by_beat(beat_of_occurrence, request_info):
    try:
        result = get_the_contributory_cause_by_beat(beat_of_occurrence)
        log(request_info)
        return result
    except Exception as e:
        log_error(e)
        return {}


def get_injuries_by_beat(beat_of_occurrence, request_info):
    try:
        filtered_documents = how_many_were_injured_and_how_many_died_in_certain_place(beat_of_occurrence)
        total_injuries_sum = 0
        fatal_injuries_sum = 0
        for doc in filtered_documents:
            total_injuries_sum += int(doc['injuries']['total'])
            fatal_injuries_sum += int(doc['injuries']['fatal'])
        list_of_died = everyone_who_died_in_a_certain_place(beat_of_occurrence)
        list_of_not_died = everyone_who_not_died_in_a_certain_place(beat_of_occurrence)
        log(request_info)
        return {"total_injuries_sum": total_injuries_sum,
                "fatal_injuries_sum": fatal_injuries_sum,
                "list_of_died": list_of_died,
                "list_of_not_died": list_of_not_died
                }
    except Exception as e:
        log_error(e)
        return {}
