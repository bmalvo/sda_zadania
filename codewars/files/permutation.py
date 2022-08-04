"""this script doing permutations_word of words"""

from itertools import permutations

# task:
# In this kata you have to create all permutations_word of a non empty.
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


# solution:


# def permutations_word(word):
#     """this func do permutation"""
#     word = list(word)
#     if len(word) == 1:
#         return word
#
#     result = []
#     end_result = []
#
#     for i in range(len(word)):
#         one = word[i]
#         other = word[:i] + word[i + 1:]
#         for per in permutations_word(other):
#             per_add = [one] + list(per)
#             if per_add not in result:
#                 result.append(per_add)
#
#         for obj in result:
#             word = ''
#             for letter in obj:
#                 word += letter
#             if word not in end_result:
#                 end_result.append(word)
#     return end_result
#
#
# print(permutations_word('abab'))
# print(permutations_word('ab'))

def all_permutations(word):
    per_iter = permutations(word)
    per_list = []
    for per in per_iter:
        if ''.join(per) not in per_list:
            per_list.append(''.join(per))
    return per_list


print(list(all_permutations('a')))
