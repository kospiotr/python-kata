import pytest

from algoexpert.assertions import assert_arrays
from src.algoexpert.easy.e_arr_01_two_number_sum import twoNumberSum_sol_1, twoNumberSum_sol_2, twoNumberSum_sol_3

test_cases = [
    ([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11]),
    ([3, 5, -4, 8, 11, 1, -1, 6], 100, []),
    ([3, 5, -4, 8, 11, 1, -1, 6], 0, [1, -1]),
    ([], 9, []),
    ([4,6],10, [4,6]),
    ([4, 6, 1],5, [4,1]),
    ([4, 6, 1, -3],3, [6,-3]),
    ([4, 6, 1, -3],3, [6,-3]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9],17, [8,9]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15],18, [3,15]),
    ([-7, -5, -3, -1, 0, 1, 3, 5, 7],-5, [-5,0]),
    ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],163, [210, -47]),
    ([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],164, []),
    ([3, 5, -4, 8, 11, 1, -1, 6],15, []),
    ([14],15, []),
    ([15],15, []),
]

@pytest.mark.parametrize("array, targetSum, result",test_cases)
def test_twoNumberSum_sol_1(array, targetSum, result):
    assert_arrays(twoNumberSum_sol_1(array, targetSum), result)

@pytest.mark.parametrize("array, targetSum, result", test_cases)
def test_twoNumberSum_sol2(array, targetSum, result):
    assert_arrays(twoNumberSum_sol_2(array, targetSum), result)

@pytest.mark.parametrize("array, targetSum, result", test_cases)
def test_twoNumberSum_sol3(array, targetSum, result):
    assert_arrays(twoNumberSum_sol_3(array, targetSum), result)

