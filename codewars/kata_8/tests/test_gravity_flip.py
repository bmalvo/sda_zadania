from codewars.kata_8.files.gravity_flip import flip
import pytest


@pytest.mark.parametrize('given, expected', [(('R', [3, 2, 1, 2]), [1, 2, 2, 3]),
                                             (('L', [1, 4, 5, 3, 5]), [5, 5, 4, 3, 1])])
def test_flip(given, expected):
    print(given[0])
    print(given[1])
    print(expected)
    assert flip(given[0], given[1]) == expected
