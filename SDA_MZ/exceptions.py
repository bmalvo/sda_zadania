"""Exceptions solvers: """

# task 1

ints_list = []

# a
ints_list.append(11)
ints_list.append(22)
ints_list.append(33)
ints_list.append(44)
ints_list.append(55)

# b
# print(ints_list[5])
# c
# output -> IndexError: list index out of range
# d, e
try:
    print(ints_list[5])
except IndexError:
    print('The list is tiny shorter.')
except:
    print("Something goes wrong.")

# task 2


def name_printer(label=''):
    name = label
    try:
        lenght_name = len(name)
        if lenght_name == 0:
            raise ValueError('Name required at least 1 character')
    finally:
        print(name)

# task 3


def division_func(num1, num2):
    try:
        result = num1/num2
        return result
    except ZeroDivisionError:
        print('ZeroDivisionError: division by zero')
        return 0

# task 4


some_dict = {
    'items': ['loundry machine', 'tv', 'vacum machine', 'fridge']
}


def get_item_with_try_except(d_ict):
    try:
        res = d_ict["items"]
        return res
    except KeyError:
        return f'This dict has not key: "items".'


def get_item_from_dict_with_get(d_ict):
    res = d_ict.get('items', 'This dict has not got key "items"')
    return res


# print(get_item_from_dict_with_get(some_dict))
# print(get_item_with_try_except(some_dict))

# task 5


class OrderItem:

    def __init__(self, num):
        self.num = num
        self.numbs_list = []

    def add_to_list(self):
        if OrderItem(self.num).is_correct():
            print(OrderItem(self.num).is_correct())
            self.numbs_list.append(self.num)

    def is_correct(self):
        if not type(self.num) == int:
            raise OrderItemError(ValueError)
        else:
            print('num must be an integer')
            return False


class OrderItemError(ValueError):
    pass

# task 6


def func_without_body():
    raise NotImplementedError('Func do nothing')
    pass


# func_without_body()

# task 7

try:
    with open('c:/not_exist/file') as f:
        print(f.readlines())
except FileNotFoundError:
    print('File doesn\'t exist')

# task 8
# For more knowledge visit the website -> https://realpython.com/python-exceptions/
