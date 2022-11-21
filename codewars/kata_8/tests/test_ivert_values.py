from codewars.kata_8.files.invert_values import invert


def test_invert():
    given = [1, -2, 3, -4, 5]
    assert invert(given) == [-1, 2, -3, 4, -5]
