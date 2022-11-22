from codewars.kata_8.files.alternating_case import to_alternating_case


def test_to_alternating_case_1():
    given = 'altERnaTIng cAsE'
    assert to_alternating_case(given) == 'ALTerNAtiNG CaSe'
