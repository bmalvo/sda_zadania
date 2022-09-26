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

def multi_by_two(x):
    return x * 2


def multi_all_list_by_two():
    numbers = [random.randint(0, 100) for _ in range(10)]
    print(numbers)
    map_numbers = map(multi_by_two, numbers)
    for _ in map_numbers:
        print(_, end=' - ')


# task 5

from array import array


def exercise_with_array():
    arr = array('i', [random.randint(100, 200) for _ in range(20)])
    print(arr)
    arr_sorted = sorted(arr)
    print(arr_sorted)
    arr_sorted_desc = sorted(arr, reverse=True)
    print(arr_sorted_desc)
