from database.connect import accidents


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
    return list(accidents.find({'beat_of_occurrence': beat_of_occurrence}, {"_id": 1}))


# Reference taken from: https://stackoverflow.com/questions/13529323/obtaining-group-result-with-group-count
def get_the_contributory_cause_by_beat(beat_of_occurrence):
    return accidents.aggregate([
        {"$match": {"beat_of_occurrence": beat_of_occurrence}},
        {"$group": {"_id": "$contributory_cause", "count": {"$sum": 1}}}
    ])


def how_many_were_injured_and_how_many_died_in_certain_place(beat_of_occurrence):
    return accidents.find(
        {"beat_of_occurrence": beat_of_occurrence},
        {"_id": 0, "injuries.total": 1, "injuries.fatal": 1}
    )


def everyone_who_died_in_a_certain_place(beat_of_occurrence):
    return list(accidents.find({"beat_of_occurrence": beat_of_occurrence}, {"injuries.fatal": {"$gt": "0"}},
                          {"crash_record_id": 1}))


def everyone_who_not_died_in_a_certain_place(beat_of_occurrence):
    return list(accidents.find(
        {"beat_of_occurrence": beat_of_occurrence}, {"injuries.fatal": '0'}, {"crash_record_id": 1}
    ))
