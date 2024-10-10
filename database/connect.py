from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')

# the data

# taxi_db = client['taxi-drivers']
# drivers = taxi_db['drivers']
# cars = taxi_db['cars']