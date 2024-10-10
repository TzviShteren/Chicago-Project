import pytest
from pymongo.collection import Collection


def test_count_of_all_accidents(accidents_collection: Collection):
    res = list(accidents_collection.find({}))
    assert len(res) == 20000
