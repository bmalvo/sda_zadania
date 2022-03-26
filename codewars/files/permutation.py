"""this script doing fun stuff"""
# task:
# In this kata you have to create all permutations of a non empty
# input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.
#
# Examples:
#
# * With input 'a'
# * Your function should return: ['a']
# * With input 'ab'
# * Your function should return ['ab', 'ba']
# * With input 'aabb'
# * Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

TEXT = 'ab'

# solution:
def permutation(sstring):
    """this class do something"""
    print(sstring)
    lst = []
    i = 0
    for chara in range(len(sstring)):
        lst.append(sstring[i])
        print(chara)
        i += 1
    print(lst)




permutation(TEXT)
