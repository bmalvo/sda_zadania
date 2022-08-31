import pytest
from codewars.files.permutation import all_permutations


@pytest.mark.parametrize('given, expected', [('ab', ['ab','ba'])])
def test_solution(given, expected):
    assert all_permutations(given) == expected


@pytest.mark.parametrize('given, expected', [('aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])])
def test2_solution(given, expected):
    assert all_permutations(given) == expected


