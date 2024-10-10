import csv
from database.connect import accidents

def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row


def init_accidents():
    accidents.drop()

    for row in read_csv('../data/Traffic_Crashes_-_Crashes - 20k rows.csv'):
        crash_date = {
            'foll_date': row['CRASH_DATE'],
            'day_of_week': row['CRASH_DAY_OF_WEEK'],
        }
        injuries = {
            'total': row['INJURIES_TOTAL'],
            'fatal': row['INJURIES_FATAL'],
        }

        accident = {
            'crash_record_id': row['CRASH_RECORD_ID'],
            'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
            'contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
            'crash_date': crash_date,
            'injuries': injuries
        }

        accidents.insert_one(accident)

