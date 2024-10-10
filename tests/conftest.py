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
def accidents_db(mongodb_client):
    db_name = 'Chicago_accidents'
    return mongodb_client[db_name]


@pytest.fixture(scope="function")
def accidents_collection(accidents_db):
    return accidents_db['accidents']
