from codewars.kata_8.files.convert_a_boolean_to_string import boolean_to_string


def test_boolean_to_string_if_true():
    b = True
    assert boolean_to_string(b) == 'True'


def test_boolean_to_string_if_false():
    b = False
    assert boolean_to_string(b) == 'False'
