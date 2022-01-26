# Task:
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word
# and an array with words. You should return an array of all the anagrams or an empty array if there are none.

# examples:

anagrams1 = ('abba', ['aabb', 'abcd', 'bbaa', 'dada'])  # => ['aabb', 'bbaa']

anagrams2 = ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])  # => ['carer', 'racer']

anagrams3 = ('laser', ['lazing', 'lazy',  'lacer'])  # => []

# solution

def anagrams(word, words):
    word = word[0].split(" ")
    word_dict = {}
    result = []
    for x in word[0]:
        word_dict[x] = word_dict.get(x, 0) +1
    for x in words:
        if len(x) == len(word[0]):
            x_dict = {}
            for y in x:
                x_dict[y] = x_dict.get(y, 0) +1
            if word_dict == x_dict:
                result.append(x)
    return result

print(anagrams(anagrams1, anagrams1[1]))

assert anagrams(anagrams1, anagrams1[1]) == ['aabb', 'bbaa']
assert anagrams(anagrams2, anagrams2[1]) == ['carer', 'racer']
assert anagrams(anagrams3, anagrams3[1]) == []

# best solution from site:
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]