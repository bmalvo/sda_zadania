""" Lambda exercises """


# task 1


nameList = ['John', 'Daemon', 'Elevryn', 'Macaray', 'Zaerniitzh']


def sort_long_asc():
    nameList.sort(key=lambda x: len(x))
    return nameList


def sort_long_desc():
    nameList.sort(key=lambda x: len(x), reverse=True)
    return nameList


def sort_first_letter_asc():
    nameList.sort()
    return nameList


