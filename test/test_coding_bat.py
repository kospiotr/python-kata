import pytest

from src.coding_bat import (
    t_01_sleep_in,
    t_02_monkey_trouble,
    t_03_sum_double,
    t_04_diff21,
    t_05_parrot_trouble,
    t_06_makes10,
    t_07_near_hundred,
)


@pytest.mark.parametrize(
    "weekday,vacation,result",
    [(False, False, True), (True, False, False), (False, True, True)],
)
def test_t_01_sleep_in(weekday, vacation, result):
    print(f"args: {weekday}, {vacation}, {result}")
    assert t_01_sleep_in(weekday, vacation) == result


@pytest.mark.parametrize(
    "a_smile, b_smile, result",
    [
        (True, True, True),
        (False, False, True),
        (True, False, False),
    ],
)
def test_t_02_monkey_trouble(a_smile, b_smile, result):
    assert t_02_monkey_trouble(a_smile, b_smile) == result


# def test_t_03_sum_double(a, b, result):
#     pass


@pytest.mark.parametrize(
    "a,b,c",
    [
        (1, 2, 3),
        (3, 3, 12),
    ],
)
def test_t_03_sum_double(a, b, c):
    assert t_03_sum_double(a, b) == c


@pytest.mark.parametrize(
    "n,result",
    [
        (21, 0),
        (20, 1),
        (22, 2),
        (25, 8),
        (0, 21),
    ],
)
def test_t_04_diff21(n, result):
    assert t_04_diff21(n) == result


@pytest.mark.parametrize(
    "talking, hour, result",
    [
        (True, 6, True),
        (True, 21, True),
        (True, 8, False),
        (False, 8, False),
        (True, 7, False),
        (True, 20, False),
    ],
)
def test_t_05_parrot_trouble(talking, hour, result):
    assert t_05_parrot_trouble(talking, hour) == result


@pytest.mark.parametrize(
    "a,b,result",
    [
        (10, 1, True),
        (1, 10, True),
        (1, 9, True),
        (9, 1, True),
        (4, 1, False),
    ],
)
def test_t_06_makes10(a, b, result):
    assert t_06_makes10(a, b) == result


@pytest.mark.parametrize(
    "n,result",
    [
        (100, True),
        (90, True),
        (91, True),
        (101, True),
        (110, True),
        (200, True),
        (190, True),
        (191, True),
        (201, True),
        (210, True),
        (89, False),
        (111, False),
        (189, False),
        (211, False),
    ],
)
def test_t_07_near_hunred(n, result):
    assert t_07_near_hundred(n) == result
