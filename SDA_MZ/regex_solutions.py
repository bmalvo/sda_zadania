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


