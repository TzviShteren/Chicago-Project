from pymongo.collection import Collection


def test_sum_of_accidents_by_beat_of_occurrence(accidents_collection: Collection):
    res = accidents_collection.count_documents({"beat_of_occurrence": '225'})
    assert res == 268