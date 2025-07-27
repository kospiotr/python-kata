import pytest
from src.algoexpert.easy.t_03_sorted_squared_array import sortedSquaredArray_sol_1, sortedSquaredArray_sol_2

test_cases = [
    ([1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81]),
    ([-3, -2, -1, 1, 2, 3, 4, 5], [1, 1, 4, 4, 9, 9, 16, 25]),
    ([1, 2, 3, 5, 6, 8, 9],[1, 4, 9, 25, 36, 64, 81]),
    ([1],[1]),
    ([1, 2],[1, 4]),
    ([1, 2, 3, 4, 5],[1, 4, 9, 16, 25]),
    ([0],[0]),
    ([10],[100]),
    ([-1],[1]),
    ([-2, -1],[1, 4]),
    ([-5, -4, -3, -2, -1],[1, 4, 9, 16, 25]),
    ([-10],[100]),
    ([-10, -5, 0, 5, 10],[0, 25, 25, 100, 100]),
    ([-7, -3, 1, 9, 22, 30],[1, 9, 49, 81, 484, 900]),
    ([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20],[0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([-1, -1, 2, 3, 3, 3, 4],[1, 1, 4, 9, 9, 9, 16]),
    ([-3, -2, -1],[1, 4, 9]),
    ([-3, -2, -1],[1, 4, 9]),
]


@pytest.mark.parametrize("input_array, result", test_cases)
def test_sortedSquaredArray_sol_1(input_array, result):
    assert sortedSquaredArray_sol_1(input_array) == result


@pytest.mark.parametrize("input_array, result", test_cases)
def test_sortedSquaredArray_sol_2(input_array, result):
    assert sortedSquaredArray_sol_2(input_array) == result
