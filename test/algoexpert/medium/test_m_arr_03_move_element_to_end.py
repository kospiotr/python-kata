import copy

import pytest

from src.algoexpert.medium.m_arr_03_move_element_to_end import moveElementToEnd_sol_1

test_cases = [
    ([2, 1, 2, 2, 2, 3, 4, 2], 2, [1, 3, 4, 2, 2, 2, 2, 2]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [1, 2, 4, 5, 6, 7, 3]),
    ([2, 1, 2, 2, 2, 3, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2, 2]),
    ([], 3, []),
    ([1, 2, 4, 5, 6], 3, [1, 2, 4, 5, 6]),
    ([3, 3, 3, 3, 3], 3, [3, 3, 3, 3, 3]),
    ([3, 1, 2, 4, 5], 3, [5, 1, 2, 4, 3]),
    ([1, 2, 4, 5, 3], 3, [1, 2, 4, 5, 3]),
    ([1, 2, 3, 4, 5], 3, [1, 2, 5, 4, 3]),
    ([2, 4, 2, 5, 6, 2, 2], 2, [6, 4, 5, 2, 2, 2, 2]),
    ([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5, [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5, 5, 5, 5]),
    ([1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5], 5, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]),
    ([5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5, [12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5])
]


@pytest.mark.parametrize("array, toMove, result_expected", copy.deepcopy(test_cases))
def test_moveElementToEnd_sol_1(array, toMove, result_expected):
    array = moveElementToEnd_sol_1(array, toMove)
    if len(array) != len(result_expected):
        assert array == result_expected
    for el_index, el_value in enumerate(result_expected):
        if el_value == toMove and array[el_index] != toMove:
            assert array == result_expected
