import pytest

from electronic_devices import atm
from electronic_devices.atm import Account, Card, NoFundsError

@pytest.fixture()
def acc():
    return atm.Account(123321, "Bob", "Marley", 1000, 0)

@pytest.fixture()
def card():
    return atm.Card(123321, 8520, 'Bob', 'Marley')



def test_account_print_account_number(acc):
    assert acc.number == 123321

@pytest.mark.parametrize("given, expected",[((acc),"Bob Marley")])
def test_acc_owner(given, expected, acc):
    assert acc.owner() == expected

@pytest.mark.parametrize("given, expected",[((acc),1000)])
def test_acc_balance_return_account_state(given, expected, acc):
    assert acc.balance() == expected

@pytest.mark.parametrize("given, expected",[((acc),123321)])
def test_acc_owner_return_acc_number(given, expected, acc):
    assert acc.number() == expected

def test_acc_number_return_acc_number(acc):
    assert acc.number() == 123321

@pytest.mark.parametrize("given, expected",[(100,1100),(-1000,0),(-500, 500)])
def test_acc_transfer_works(given, expected, acc):
    assert acc.transfer(operation=given) == expected

@pytest.mark.parametrize('given, expected',[(-1100,NoFundsError)])
def test_transfer_raise_NoFundsError(given, expected, acc):
    with pytest.raises(expected):
        acc.transfer(operation=given)

# @pytest.mark.parametrize('given, expected',[(8520,8520)])
# def test_Card_check_pin(given, expected, acc):
#     assert atm.Card.check_pin() == expected

