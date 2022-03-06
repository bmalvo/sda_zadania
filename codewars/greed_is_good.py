# task:
# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a
# throw according to these rules. You will always be given an array with five six-sided dice values.
#
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
#
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
# (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
#
# Example scoring
#
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

# Solution:

dice_2 = [2, 4, 4, 5, 4]

def score(dice):
    dic = {}
    scores = 0
    for i in dice:
        dic[i] = dic.get(i,0)+1
    for k, v in dic.items():
        if k == 1:
            if v == 5:
                scores += 1200
            if v == 4:
                scores += 1100
            if v == 3:
                scores += 1000
            if v == 2:
                scores += 200
            if v == 1:
                scores += 100
        if k == 6:
            if v in (5, 4, 3):
                scores += 600
        if k == 5:
            if v == 5:
                scores += 600
            if v == 4:
                scores += 550
            if v == 3:
                scores += 500
            if v == 2:
                scores += 100
            if v == 1:
                scores += 50
        if k == 4:
            if v in (5, 4, 3):
                scores += 400
        if k == 3:
            if v in (5, 4, 3):
                scores += 300
        if k == 2:
            if v in (5, 4, 3):
                scores += 200
    return scores


print(score(dice_2))