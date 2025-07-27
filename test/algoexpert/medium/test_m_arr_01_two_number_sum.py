import copy

import pytest

from src.algoexpert.medium.m_arr_01_two_number_sum import threeNumberSum_sol_1, threeNumberSum_sol_2

test_cases = [
    ([12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]),
    ([-8, -6, 1, 2, 3, 5, 6, 12], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]),
    ([], 0, []),
    ([1, 2, 3], 6, [[1, 2, 3]]),
    # ([-2, -2, -1, -1, 0, 0, 1, 1, 2, 2], 0, [[-2, 0, 2],
    #                                          [-2, 0, 2],
    #                                          [-2, 0, 2],
    #                                          [-2, 0, 2],
    #                                          [-2, 1, 1],
    #                                          [-2, 0, 2],
    #                                          [-2, 0, 2],
    #                                          [-2, 0, 2],
    #                                          [-2, 0, 2],
    #                                          [-2, 1, 1],
    #                                          [-1, -1, 2],
    #                                          [-1, -1, 2],
    #                                          [-1, 0, 1],
    #                                          [-1, 0, 1],
    #                                          [-1, 0, 1],
    #                                          [-1, 0, 1],
    #                                          [-1, 0, 1],
    #                                          [-1, 0, 1],
    #                                          [-1, 0, 1],
    #                                          [-1, 0, 1]]),
    ([-2, -1, 0, 1, 2], 0, [[-2, 0, 2], [-1, 0, 1]]),
    ([12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]),
    ([1, 2, 3], 6, [[1, 2, 3]]),
    ([1, 2, 3], 7, []),
    ([8, 10, -2, 49, 14], 57, [[-2, 10, 49]]),
    ([12, 3, 1, 2, -6, 5, 0, -8, -1], 0, [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]]),
    ([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]]),
    ([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0, [[-8, 2, 6],
                                                 [-8, 3, 5],
                                                 [-6, 0, 6],
                                                 [-6, 1, 5],
                                                 [-5, -1, 6],
                                                 [-5, 0, 5],
                                                 [-5, 2, 3],
                                                 [-1, 0, 1]]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [[1, 2, 15],
                                           [1, 8, 9],
                                           [2, 7, 9],
                                           [3, 6, 9],
                                           [3, 7, 8],
                                           [4, 5, 9],
                                           [4, 6, 8],
                                           [5, 6, 7]]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32, [[8, 9, 15]]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33, []),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5, [])
]


@pytest.mark.parametrize("input_array, target_sum, result_expected", copy.deepcopy(test_cases))
def test_threeNumberSum_sol_1(input_array, target_sum, result_expected):
    assert threeNumberSum_sol_1(input_array, target_sum) == result_expected

@pytest.mark.parametrize("input_array, target_sum, result_expected", copy.deepcopy(test_cases))
def test_threeNumberSum_sol_2(input_array, target_sum, result_expected):
    assert threeNumberSum_sol_2(input_array, target_sum) == result_expected
