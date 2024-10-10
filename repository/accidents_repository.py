from database.connect import accidents


def sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence):
    return accidents.count_documents({"beat_of_occurrence": beat_of_occurrence})
