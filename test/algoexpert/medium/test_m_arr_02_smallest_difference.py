import copy

import pytest

from src.algoexpert.medium.m_arr_02_smallest_difference import smallestDifference_sol_1, smallestDifference_sol_2

test_cases = [
    (
        [-1,  3,  5,  10,  20, 28, 50],
        [15, 17, 26, 50, 134, 135],
        [50, 50]
    ),
    ([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26]),
    ([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17], [20, 17]),
    ([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031], [25, 1005]),
    ([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031], [25, 1005]),
    ([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031], [2000, 1032]),
    ([240, 124, 86, 111, 2, 84, 954, 27, 89], [1, 3, 954, 19, 8], [954, 954]),
    ([0, 20], [21, -2], [20, 21]),
    ([10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [1000, 1014]),
    ([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [-123, -124]),
    ([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530], [530, 530])
]


@pytest.mark.parametrize("arrayOne, arrayTwo, result_expected", copy.deepcopy(test_cases))
def test_smallestDifference_sol_1(arrayOne, arrayTwo, result_expected):
    assert smallestDifference_sol_1(arrayOne, arrayTwo) == result_expected


@pytest.mark.parametrize("arrayOne, arrayTwo, result_expected", copy.deepcopy(test_cases))
def test_smallestDifference_sol_2(arrayOne, arrayTwo, result_expected):
    assert smallestDifference_sol_2(arrayOne, arrayTwo) == result_expected
