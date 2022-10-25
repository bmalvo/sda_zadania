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


print(get_item_from_dict_with_get(some_dict))
print(get_item_with_try_except(some_dict))
