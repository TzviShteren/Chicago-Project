from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

# the data

Chicago_accidents_db = client['Chicago_accidents']
accidents = Chicago_accidents_db['accidents']