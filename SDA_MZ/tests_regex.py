import pytest
from SDA_MZ.regex_solutions import code_validator, login_validator, search_validator, \
                                   data_validator, serial_validator


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


def test_data_validator_valid():
    assert data_validator('10.02.2018r') == 'Valid date'


def test_data_validator_invalid():
    assert data_validator('10,03,2018r') == 'Invalid date'


def test_serial_validator_valid():
    assert serial_validator('VSD43281fA') == 'Valid serial'


def test_serial_validator_invalid():
    assert serial_validator('VSDe3281fa') == 'Invalid serial'
