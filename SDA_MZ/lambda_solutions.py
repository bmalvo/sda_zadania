""" Lambda exercises """


# task 1
import random

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


# task 3

def biggest_cash():
    biggest_account = max(account_list, key=lambda x: x.balance)
    return biggest_account.name


# task 4

def multiplied_by_two():
    numbers = [x for x in random.randrange(1,100)]
    ten_numbers = random.randint(numbers)
    print(ten_numbers)