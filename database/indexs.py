from database.connect import accidents


def creat_indexs():
    accidents.create_index({'beat_of_occurrence': 1})

    accidents.create_index([("beat_of_occurrence", 1), ("crash_date.day_of_week", 1)])

    accidents.create_index([("beat_of_occurrence", 1), ("crash_date.foll_date", 1)])

    accidents.create_index([("contributory_cause", 1)])

    accidents.create_index([("injuries.fatal", 1)])
