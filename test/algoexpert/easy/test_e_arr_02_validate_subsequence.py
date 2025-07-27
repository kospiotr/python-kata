import pytest
from src.algoexpert.easy.e_arr_02_validate_subsequence import isValidSubsequence_sol_1, isValidSubsequence_sol_2, \
    isValidSubsequence_sol_3

test_cases = [
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
    ([5, 1, 22, 25, 5, -1, 8, 10], [1, 6, -1, 10], False),
    ([], [1, 6, -1, 10], False),
    ([5], [1, 6, -1, 10], False),
    ([1, 2, 3, 4], [1, 3, 4], True),
    ([1, 2, 3, 4], [2, 4], True),
    ([1, 2, 3, 4], [1], True),
    ([1, 2, 3, 4], [2], True),
    ([1, 2, 3, 4], [4], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, -1, 8, 10], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [25], True),
    ([1, 1, 1, 1, 1], [1, 1, 1], True),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [4, 5, 1, 22, 25, 6, -1, 8, 10], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 25, 6, -1, 8, 10], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1, 10], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -2], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [26], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 26, 22, 8], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 1, 1, 6], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 10], False),
    ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 5], False),
]


@pytest.mark.parametrize("input_array, input_sequence, result", test_cases)
def test_isValidSubsequence_sol_1(input_array, input_sequence, result):
    assert isValidSubsequence_sol_1(input_array, input_sequence) == result

@pytest.mark.parametrize("input_array, input_sequence, result", test_cases)
def test_isValidSubsequence_sol_2(input_array, input_sequence, result):
    assert isValidSubsequence_sol_2(input_array, input_sequence) == result

@pytest.mark.parametrize("input_array, input_sequence, result", test_cases)
def test_isValidSubsequence_sol_3(input_array, input_sequence, result):
    assert isValidSubsequence_sol_3(input_array, input_sequence) == result