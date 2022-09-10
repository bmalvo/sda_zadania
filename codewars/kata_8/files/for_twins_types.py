"""Task:
Write a function that will accept two parameters: variable and type and check
if type of variable is matching type. Return true if types match or false if not.

Examples:
42, "int"    --> True
"42", "int"  --> False"""
from collections import Counter
from pandas._libs.hashtable import Vector
from pandas.compat.numpy import function
from pandas import DataFrame
from re import A

B = type(bytes)
NoneType = type(None)


def type_validation(vaariable, _type):
    return isinstance(vaariable, (eval(_type)))
