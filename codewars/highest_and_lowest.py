# Task:

# Return the highest and the lowest numbers from the string


# Examples:

numbers_1 = ("1 2 3 4 5")  # return "5 1"
numbers_2 = ("1 2 -3 4 5") # return "5 -3"
numbers_3 = ("1 9 3 4 -5") # return "9 -5"
numbers_4 = ("929 -278 -237 -402 -671 -694 373 533 381 -25 996 320 -687 863 711") # return "996 -694"


# Solution:


def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers2 = []
    for x in numbers:
        try:
            numbers2.append(int(x))
        except ValueError:
            numbers2.append(int(x))
    numbers = str(max(numbers2))+' '+str(min(numbers2))
    return numbers


print(high_and_low(numbers_1))
print(high_and_low(numbers_2))
print(high_and_low(numbers_3))
print(high_and_low(numbers_4))

