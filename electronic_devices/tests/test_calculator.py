import io

import pytest

from electronic_devices import calculator
from electronic_devices.calculator import Calculator, NoBatteryError, NoFileDefinedError


@pytest.fixture()
def calc():
    """ Inicjalizacja obiektu klasy Calculator """
    # Given
    return Calculator()


def test_init_calculator(calc):
    assert calc.battery == 100
    assert calc.memory == 0


@pytest.mark.parametrize("given_value,expected_value", [(0, NoBatteryError), (-5, NoBatteryError)])
def test_init_calculator_raise_battery_error(given_value, expected_value):
    with pytest.raises(expected_value):
        calc = Calculator(battery=given_value)


def test_check_add_5_3_return_8(calc):
    # When
    result = calc.add(5, 3)
    # Then
    assert result == 8


@pytest.mark.parametrize("given_values,expected_result",
                         [((1, 2, 3, 4), 10), ((-10, 5, -7, 32), 20), ((0, -100.50, 200), 99.50)])
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
        calc.add(2, 2)


def test_check_raise_no_battery_error_when_subtract(calc):
    calc.battery = 1
    assert calc.subtract(2, 2) == 0
    with pytest.raises(NoBatteryError):
        calc.add(2, 2)


def test_check_multiply(calc):
    assert calc.multiply(2, 2, 2) == 8
    assert calc.memory == 8


def test_check_divide(calc):
    assert calc.divide(20, 10, 2) == 1
    assert calc.memory == 1


def test_check_divide_by_0(calc):
    with pytest.raises(ValueError):
        calc.divide(1, 2, 5, 0, 20)


def test_check_to_nth_power(calc):
    assert calc.to_nth_power(10, 2) == 100
    assert calc.to_nth_power(1.1, 2) == 1.21


def test_check_is_even(calc):
    assert calc.is_even(66) is True
    assert calc.memory is True
    assert calc.is_even(33) is False
    assert calc.memory is False


def test_check__get_data(mocker):
    fake_file = io.StringIO("1,2\n2,2,2\n1,1,1,5,2")
    mocker.patch("electronic_devices.calculator.os")
    mocker.patch("electronic_devices.calculator.open", return_value=fake_file, create=True)
    calc = Calculator()
    calc.file = "fake_file.txt"

    assert calc._get_data() == [[1, 2], [2, 2, 2], [1, 1, 1, 5, 2]]
    calculator.open.assert_called_once()
    calculator.open.assert_called_once_with("fake_file.txt")
    calculator.os.path.isfile.assert_called_once()


def test_check_avg_form_file_raise_no_file_defined_error(calc):
    with pytest.raises(NoFileDefinedError):
        calc.avg_from_file()


def test_check_avg_form_file_raise_file_not_found_error(calc):
    calc.file = "cokolwiek"
    with pytest.raises(FileNotFoundError):
        calc.avg_from_file()


def test_check_avg_from_file(mocker):
    mocker.patch("electronic_devices.calculator.Calculator._get_data",
                 return_value=[[1, 2], [2, 2, 2], [1, 1, 1, 5, 2]])
    expected = [1.5, 2.0, 2.0]
    calc = Calculator()
    actual = calc.avg_from_file()
    assert expected == actual
    calc._get_data.assert_called_once()
