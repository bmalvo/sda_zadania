"""Task:
Write a function that will accept two parameters: variable and type and check
if type of variable is matching type. Return true if types match or false if not.

Examples:
42, "int"    --> True
"42", "int"  --> False"""


def type_validation(variable, _type):
    try:
        res = variable == _type
    except TypeError:
        res = False
    return res
    # your code here
    pass


print(type_validation('2', int))
print(2 == int)
