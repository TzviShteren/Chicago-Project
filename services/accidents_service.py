from services.logger import *
from repository.accidents_repository import *


def get_sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence, request_info):
    try:
        result = sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence)
        log(request_info)
        return result.inserted_id
    except Exception as e:
        log_error(e)
        return {}
