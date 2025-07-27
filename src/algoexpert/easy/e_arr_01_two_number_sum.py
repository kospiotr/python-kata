"""
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.


Note that the target sum has to be obtained by summing two different integers
in the array; you can't add a single integer to itself in order to obtain the
target sum.

You can assume that there will be at most one pair of numbers summing up to
the target sum.

Sample Input
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sample Output
[-1, 11] // the numbers could be in reverse order
"""


# noinspection PyPep8Naming
def twoNumberSum_sol_1(array, targetSum) -> list[str]:
    """
    Brute force solution.
    """
    for l_index in range(len(array) - 1):
        for r_index in range(l_index + 1, len(array)):
            l_value = array[l_index]
            r_value = array[r_index]
            if l_value + r_value == targetSum:
                return [l_value, r_value]
    return []


def twoNumberSum_sol_2(array, targetSum) -> list[str]:
    """
    Using hash table for diff lookup
    """
    collector = set()

    for el in array:
        diff = targetSum - el
        if diff in collector:
            return [el, diff]
        collector.add(el)
    return []


def twoNumberSum_sol_3(array, targetSum) -> list[str]:
    """
    Sorting array and use two pointers
    """

    array.sort()

    l_index = 0
    r_index = len(array) - 1

    while l_index < r_index:
        l_value = array[l_index]
        r_value = array[r_index]
        sum = l_value + r_value
        if sum == targetSum:
            return [l_value, r_value]
        elif sum < targetSum:
            l_index += 1
        elif sum > targetSum:
            r_index -= 1

    return []
