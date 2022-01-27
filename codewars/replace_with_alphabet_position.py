# Task:
#
# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

# Example:

txt = "The sunset sets at twelve o' clock." # --> "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5
                                             # 15 3 12 15 3 11"
# Solutin:

alphabet = {chr(i+96): i for i in range(1, 27)}

def alphabet_position(text):
    text = text.lower()
    text = list(text)
    new_text = []
    for chr in text:
        if chr in alphabet:
            new_text.append(alphabet[chr])
    result = " ".join(str(x) for x in new_text)
    return result


print(alphabet_position(txt))