import pytest

from electronic_devices import atm
from electronic_devices.atm import Account, Card

@pytest.fixture()
def acc():
    return atm.Account(123321,"Bob","Marley",1000,0)

@pytest.fixture()
def card():
    return atm.Card



# def test_account_print_accpunt_number(acc):
#     assert acc.account_number == acc.account_number

@pytest.mark.parametrize("given, expected",[((),"Bob Marley")])
def test_acc_owner(given,expected,acc):
    assert acc.owner(given) == expected


