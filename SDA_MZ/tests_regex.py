import pytest
from SDA_MZ.regex_solutions import code_validator, login_validator, search_validator


def test_code_validator_1():
    assert code_validator('85-155') == 'This is a valid code. Thanks!'


def test_code_validator_2():
    assert code_validator('00-122') == 'This is a valid code. Thanks!'


def test_code_validator_fail():
    assert code_validator('22.334') == 'This code is invalid.'


@pytest.mark.xfail
def test_code_validator_failed():
    if code_validator(22-222):
        pytest.xfail('input should be string')


def test_login_validation_valid():
    assert login_validator('BillyJoe33') == 'This is a valid login.'


def test_login_validation_invalid():
    assert login_validator('short') == 'This login is invalid.'


def test_search_validator_find():
    assert search_validator('koala') == 'Find one match'


def test_search_validator_no_mach():
    assert search_validator('tiger') == 'There is no match'
    