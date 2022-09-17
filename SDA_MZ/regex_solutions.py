"""Here are answers to regex_task.txt"""

import re
# task 1


# def checking_input():
#     """ Checking input characteristics"""
#     number = input("Type some number: ")
#     if not number.isdigit():
#         print(f'Your input:"{number}" is not a integer. Try again: ')
#         checking_input()
#     else:
#         even_or_odd = (int(number) % 2 == 0)
#         if even_or_odd:
#             res = f'Your number: {number} is even'
#         else:
#             res = f'Your number: {number} is odd'
#         return res
#
#
# print(checking_input())

# Task 2

def code_validator(post_code):
    """checking if a post code is valid"""
    pattern = '[0-9]{2}-[0-9]{3}'
    if re.fullmatch(pattern, post_code):
        res = 'This is a valid code. Thanks!'
    else:
        res = 'This code is invalid.'
    return res

# Task 3


def login_validator(your_login):
    pattern = '[a-zA-Z0-9]{8,16}'
    if re.fullmatch(pattern, your_login):
        res = 'This is a valid code. Thanks!'
    else:
        res = 'This code is invalid.'
    return res

# Task 4


def search_validator(text):
    pattern = 'ala'
    if re.search(pattern, text):
        res = 'Find one match'
    else:
        res = 'There is no match'
    return res

# Task 5


def data_validator(date):
    pattern = r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}r'
    if re.fullmatch(pattern, date):
        res = 'Valid date'
    else:
        res = 'Invalid date'
    return res

# Task 6


def serial_validator(serial):
    pattern = '[A-Z]{3}[0-9]{5}[a-z][A-Z]'
    if re.fullmatch(pattern, serial):
        res = 'Valid serial'
    else:
        res = 'Invalid serial'
    return res

# Task 7


def serial_number_validator(serial_number):
    pattern = '[A-Z0-9&]{5}-[A-Z0-9&]{5}-[A-Z0-9&]{5}-[A-Z0-9&]{5}-[A-Z0-9&]{5}'
    if re.fullmatch(pattern, serial_number):
        res = 'Valid serial number'
    else:
        res = 'Invalid serial number'
    return res

# Task 8


def invoice_validator(invoice):
    pattern = '(FV)/1[0-9]{3}/(0[1-9]|1[012])/[0-9]{4}'
    if re.fullmatch(pattern, invoice):
        res = 'Valid invoice'
    else:
        res = 'Invalid invoice'
    return res


