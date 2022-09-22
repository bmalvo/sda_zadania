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


# task 2


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


aron = BankAccount('Aron', 1000)
bill = BankAccount('Bill', 4000)
cecylia = BankAccount('Cecylia', 5000)
david = BankAccount('David', 7500)
egon = BankAccount('Egon', 10000)


account_list = [aron, bill, cecylia, david, egon]

big_account = filter(lambda x: x.balance > 4500, account_list)

print([x.name for x in big_account])
