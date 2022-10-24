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

