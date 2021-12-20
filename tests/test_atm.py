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

@pytest.mark.parametrize("given, expected",[((acc),('Bob', 'Marley'))])
def test_acc_owner_return_name_and_surname(given,expected,acc):
    assert acc.owner() == expected

@pytest.mark.parametrize("given, expected",[((acc),1000)])
def test_acc_balance_return_account_state(given,expected,acc):
    assert acc.balance() == expected

@pytest.mark.parametrize("given, expected",[((acc),123321)])
def test_acc_owner_return_acc_number(given,expected,acc):
    assert acc.number() == expected

def test_acc_owner_return_acc_number(acc):
    assert acc.number() == 123321

@pytest.mark.parametrize("given, expected",[(100,1100),(-1000,0),(-1010,"You have no money!")])
def test_acc_transfer_works(given,expected,acc):
    assert acc.transfer(deposit=given) == expected