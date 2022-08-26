from codewars.kata_8.files.name_on_bilboard import billboard
import pytest


@pytest.mark.parametrize('given, expected', [(),(),(),(),()])
def test_billboard():
    assert billboard(given) == expected