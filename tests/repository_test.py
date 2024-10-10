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
    assert len(list(res)) == 22


def test_how_many_were_injured_and_how_many_died_in_certain_place(accidents_collection: Collection):
    res = accidents_collection.find(
        {"beat_of_occurrence": "225"},
        {"_id": 0, "injuries.total": 1, "injuries.fatal": 1}
    )
    assert len(list(res)) == 268


def test_everyone_who_died_in_a_certain_place(accidents_collection: Collection):
    res = list(accidents_collection.find(
        {"beat_of_occurrence": "1655", "injuries.fatal": {"$gt": "0"}},
        {"_id": 0, "crash_record_id": 1}
        ))
    assert len(res) == 1


def test_everyone_who_not_died_in_a_certain_place(accidents_collection: Collection):
    res = list(accidents_collection.find(
        {"beat_of_occurrence": "1655", "injuries.fatal": "0"},
        {"_id": 0, "crash_record_id": 1}
    ))
    assert len(res) == 223
