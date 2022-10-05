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


printing_hello('Text printed before func.', 'Text printed after func.')
