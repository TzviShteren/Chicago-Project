from database.connect import accidents
from utils.dates_f import *


def sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence):
    return accidents.count_documents({"beat_of_occurrence": beat_of_occurrence})


def sum_of_accidents_by_beat_end_day(beat_of_occurrence, day):
    return accidents.count_documents({
        "beat_of_occurrence": beat_of_occurrence,
        "crash_date.day_of_week": day})


def sum_of_accidents_by_beat_end_month(beat_of_occurrence, month):
    return accidents.count_documents({
        "beat_of_occurrence": beat_of_occurrence,
        "crash_date.month": month})


def get_all_accidents_by_beat(beat_of_occurrence):
    return list(accidents.find({'beat_of_occurrence': beat_of_occurrence}, {"_id": False}))


# Reference taken from: https://stackoverflow.com/questions/13529323/obtaining-group-result-with-group-count
def get_the_contributory_cause_by_beat(beat_of_occurrence):
    return accidents.aggregate([
        {"$match": {"beat_of_occurrence": beat_of_occurrence}},
        {"$group": {"_id": "$contributory_cause", "count": {"$sum": 1}}}
    ])
