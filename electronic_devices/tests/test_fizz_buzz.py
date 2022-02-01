import pytest

from tdd.fizz_buzz import fizz_buzz

@pytest.mark.parametrize("given_value, expected_result", [(1,"1"),(2,"2"),(4,"4"),(7,"7"),(8,"8")])
def test_fizz_buzz_return_int_to_str(given_value, expected_result):
    assert fizz_buzz(given_value) == expected_result

@pytest.mark.parametrize("given_value, expected_result", [(3, "Fizz"),(5, "Buzz"),(6,"Fizz"),(10,"Buzz")])
def test_fizz_buzz_return_fizz_or_buzz(given_value,expected_result):
    assert fizz_buzz(given_value) == expected_result

@pytest.mark.parametrize("given_value, expected_result", [(15, "FizzBuzz"),(30, "FizzBuzz"),(45,"FizzBuzz")])
def test_fizz_buzz_return_fizzbuzz(given_value,expected_result):
    assert fizz_buzz(given_value) == expected_result