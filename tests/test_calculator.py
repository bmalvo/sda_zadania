import pytest

from electronic_devices.calculator import Calculator, NoBatteryError


@pytest.fixture()
def calc():
    # Given
    return Calculator()


def test_init_calculator(calc):
    assert calc.battery == 100
    assert calc.memory == 0


@pytest.mark.parametrize("given_value,expected_value", [(0, NoBatteryError), (-5, NoBatteryError)])
def test_init_calculator_raise_value_error(given_value, expected_value):
    with pytest.raises(expected_value):
        calc = Calculator(battery=given_value)


def test_check_add_5_3_return_8(calc):
    # When
    result = calc.add(5, 3)
    # Then
    assert result == 8


@pytest.mark.parametrize("given_values,expected_result",
                         [((1, 2, 3, 4), 10), ((-10, 5, -7, 32), 20), ((0, -100.50, 200), 99.50),((0,7),7)])
def test_check_add(given_values, expected_result, calc):
    assert calc.add(*given_values) == expected_result
    assert calc.memory == expected_result
    assert calc.battery == 99


@pytest.mark.parametrize("given_values,expected_result",
                         [((1, 2, 3, 4), -8), ((-10, 5, -5, -20), 10), ((-10.50, 0, 20), -30.50)])
def test_check_subtract(given_values, expected_result, calc):
    assert calc.subtract(*given_values) == expected_result
    assert calc.memory == expected_result
    assert calc.battery == 99

def test_check_raise_no_battery_error_when_add(calc):
    calc.battery = 1
    assert calc.add(2, 2) == 4
    with pytest.raises(NoBatteryError):
        calc.add(2,2)

@pytest.mark.parametrize("given_values,expected_result",
                         [((1, 2, 3, 4), 24), ((5, 4, 9, 0), 0), ((-10.50, 1, 20), -210)])
def test_check_multiply(given_values, expected_result, calc):
    assert calc.multiply(*given_values) == expected_result
    assert calc.memory == expected_result
    assert calc.battery == 99

@pytest.mark.parametrize("given_values,expected_result",
                         [((10,2), 5), ((0,1), 0), ((5,10), 0.5)])
def test_check_divide(given_values,expected_result, calc):
    dividend = given_values[0]
    divisor = given_values[1]
    assert calc.divide(dividend, divisor) == expected_result
    assert calc.memory == expected_result
    assert calc.battery == 99