""" Decorators solutions"""

# task 1


def before_after(func):
    def inner(before, after):
        print(before)
        print('---'*5)
        func()
        print('---'*5)
        print(after)
    return inner


@before_after
def printing_hello():
    print('Hello!')


# printing_hello('Text printed before func.', 'Text printed after func.')

# task2

import os


def if_exist(func):
    def wrapper(*args):
        if os.path.isfile(*args):
            return func(*args)
        else:
            new_file = open(*args, 'x', encoding='utf-8')
            return f'File  didn\'t existed. Created new.'
    return wrapper


@if_exist
def reader(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
