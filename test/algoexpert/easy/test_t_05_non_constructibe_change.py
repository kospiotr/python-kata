import pytest

from src.algoexpert.easy.t_05_non_constructibe_change import nonConstructibleChange_sol_1, nonConstructibleChange_sol_2

test_cases = [
    ([5, 7, 1, 1, 2, 3, 22], 20),
    ([1, 1, 2, 3, 5, 7, 22], 20),
    ([1, 1, 2, 3, 22], 8),
    ([1, 1, 2, 2, 22], 7),
    ([3], 1),
    ([1], 2),
    ([1, 2], 4),
    ([1, 2, 7], 4),
    ([1, 2, 3], 7),
    ([1, 2, 3, 7], 14),
    ([5, 7, 1, 1, 2, 3, 22], 20),
    ([1, 1, 1, 1, 1], 6),
    ([1, 5, 1, 1, 1, 10, 15, 20, 100], 55),
    ([6, 4, 5, 1, 1, 8, 9], 3),
    ([], 1),
    ([87], 1),
    ([5, 6, 1, 1, 2, 3, 4, 9], 32),
    ([5, 6, 1, 1, 2, 3, 43], 19),
    ([1, 1], 3),
    ([2], 1),
    ([1], 2),
    ([109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4], 87),
    ([1, 2, 3, 4, 5, 6, 7], 29)

]

@pytest.mark.parametrize("coins, result_expected", test_cases)
def test_nonConstructibleChange_sol_1(coins, result_expected):
    assert nonConstructibleChange_sol_1(coins) == result_expected

@pytest.mark.parametrize("coins, result_expected", test_cases)
def test_nonConstructibleChange_sol_2(coins, result_expected):
    assert nonConstructibleChange_sol_2(coins) == result_expected
