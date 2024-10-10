import pytest
from pymongo import MongoClient
from database.connect import Chicago_accidents_db
from repository.csv_repository import init_accidents


@pytest.fixture(scope="function")
def mongodb_client():
    client = MongoClient('mongodb://localhost:27017')
    yield client
    client.close()


@pytest.fixture(scope="function")
def accidents_test(mongodb_client):
    db_name = 'test_Chicago_accidents_db'
    db = mongodb_client[db_name]
    yield db
    mongodb_client.drop_database(db_name)


@pytest.fixture(scope="function")
def init_test_data(accidents_test):
    # Initialize the main database if it's empty
    if Chicago_accidents_db['accidents'].count_documents({}) == 0:
        init_accidents()

    # Copy data from main database to test database
    for collection_name in Chicago_accidents_db.list_collection_names():
        accidents_test[collection_name].drop()
        accidents_test[collection_name].insert_many(Chicago_accidents_db[collection_name].find())

    yield accidents_test

    # Clean up test data after each test
    for collection_name in accidents_test.list_collection_names():
        accidents_test[collection_name].drop()
