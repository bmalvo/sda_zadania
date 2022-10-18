import pickle

# task 1

list_of_objects = ['stefka', 'brydzia', 3, {'cat': 'stefka', 'turtle': 'Leon'}]

with open('pickle_file', 'ab') as f:
    pickle.dump(list_of_objects, f)

    