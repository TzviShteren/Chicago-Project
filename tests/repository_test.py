from pymongo.collection import Collection


def test_sum_of_accidents_by_beat_of_occurrence(accidents_collection: Collection):
    res = accidents_collection.count_documents({"beat_of_occurrence": '225'})
    assert res == 268


def test_sum_of_accidents_by_beat_end_day(accidents_collection: Collection):
    res = accidents_collection.count_documents({
        "beat_of_occurrence": '225',
        "crash_date.day_of_week": '3'})
    assert res == 41


def test_sum_of_accidents_by_beat_end_month(accidents_collection: Collection):
    res = accidents_collection.count_documents({
        "beat_of_occurrence": '225',
        "crash_date.month": '9'})
    assert res == 20


def test_get_the_contributory_cause_by_beat(accidents_collection: Collection):
    res = accidents_collection.aggregate([
        {"$match": {"beat_of_occurrence": "225"}},
        {"$group": {"_id": "$contributory_cause", "count": {"$sum": 1}}}
    ])
    print(list(res))
    assert 20 == 20
