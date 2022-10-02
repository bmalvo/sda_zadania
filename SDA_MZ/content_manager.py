""" Content_manager_tasks solutions"""

# task 1:


def reader(file):
    read = open(file, encoding='utf-8')
    yield read.read()


print(next(reader(r'inwokacja')))
