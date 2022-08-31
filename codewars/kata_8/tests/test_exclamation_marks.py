from codewars.kata_8.files.remove_exclamation_marks import remove_exclamation_marks
import pytest


@pytest.mark.parametrize('given, expected',
                         [("Hello World!", "Hello World"), ("Hello World!!!", "Hello World"),
                          ("", ""), ("Oh, no!!!", "Oh, no"),
                          ("Hi! Hi!", "Hi Hi"), ("Hi", "Hi")])
def test_remove(given, expected):
    assert remove_exclamation_marks(given) == expected
