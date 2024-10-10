from database.connect import accidents


def creat_indexs():
    accidents.create_index({'beat_of_occurrence': 1})
