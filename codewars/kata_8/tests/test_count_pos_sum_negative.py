from codewars.kata_8.files.count_pos_sum_negative import count_positives_sum_negatives


def test_count_positives_sum_negatives():
    testing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    assert count_positives_sum_negatives(testing_list) == [10, -65]
