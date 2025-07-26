# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
def t_01_sleep_in(weekday, vacation):
    return vacation or not weekday


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling.
# Return True if we are in trouble.
def t_02_monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or not (a_smile or b_smile)


# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.
def t_03_sum_double(a, b):
    sum = a + b
    return 2 * sum if a == b else sum


# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.
def t_04_diff21(n):
    diff = 21 - n if n <= 21 else n - 21
    if n > 21:
        return diff * 2
    else:
        return diff


# We have a loud talking parrot. The "hour" parameter is the current
# hour time in the range 0..23. We are in trouble if the parrot is
# talking and the hour is before 7 or after 20. Return True if we
# are in trouble.
def t_05_parrot_trouble(talking: bool, hour: int):
    return False if 7 <= hour <= 20 else talking


# Given 2 ints, a and b, return True if one if them is 10 or if
# their sum is 10.
def t_06_makes10(a, b):
    return a + b == 10 or a == 10 or b == 10


# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.
def t_07_near_hundred(n: int) -> bool:
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


def t_08() -> bool:
    return False
