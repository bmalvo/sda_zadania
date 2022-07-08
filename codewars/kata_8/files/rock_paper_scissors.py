""" Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!" """


def rps(p1, p2):
    """ Func output outcome of the game"""
    weapons = ['scissors', 'rock', 'paper']
    if p1 == p2:
        return 'Draw!'
    if (p1 == weapons[0] and p2 == weapons[2]) or (p1 == weapons[1] and p2 == weapons[0]) \
            or (p1 == weapons[2] and p2 == weapons[1]):
        outcome = '1'
    else:
        outcome = '2'
    return f'Player {outcome} won!'
