import pickle

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


de_pickling_data()
