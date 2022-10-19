import pickle
import csv

# task 1

list_of_objects = ['stefka', 'brydzia', 3, {'cat': 'stefka', 'turtle': 'Leon'}]


def pickling_data():
    with open('pickle_file', 'ab') as f:
        pickle.dump(list_of_objects, f)


# task 2

def de_pickling_data():
    with open('pickle_file', 'rb') as f:
        objects_list = pickle.load(f)
        for line in objects_list:
            print(line)


# de_pickling_data()

# task 3

tuple_list = [('John', 'Wick', 45342356980), ('Viseris', 'Targarien', 43546887901),
              ('Hubba', 'Bubba', 31234567890)]


def write_data_csv():
    with open('users_data.txt', 'w') as users:
        data_writer = csv.writer(users)
        data_writer.writerow(tuple_list)


# write_data_csv()

# task 4

def reader_data_csv():
    with open('users_data.txt', 'r') as users:
        data_reader = csv.reader(users)
        for row in data_reader:
            print(row)
            

reader_data_csv()
