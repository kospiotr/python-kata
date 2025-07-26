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
    arr_len = len(array)
    out = []
    for l_index in range(arr_len - 1):
        for r_index in range(l_index + 1, arr_len):
            l_value = array[l_index]
            r_value = array[r_index]
            if l_value + r_value == targetSum:
                out.append(l_value)
                out.append(r_value)

    return out

def twoNumberSum_sol_2(array, targetSum) -> list[str]:
    """
    Using hash table for diff lookup
    """
    hash_table=set()
    out = []
    for el in array:
        diff = targetSum - el
        if diff in hash_table:
            out.append(el)
            out.append(diff)
        hash_table.add(el)

    return out
def twoNumberSum_sol_3(array, targetSum) -> list[str]:
    """
    Sorting array and use two pointers
    """

    out = []
    array.sort()
    print(array)
    array_len = len(array)
    l_index = 0
    r_index = array_len - 1
    while l_index < r_index < array_len:
        l_value = array[l_index]
        r_value = array[r_index]
        sum = l_value + r_value
        print(l_index, l_value, r_index, r_value, sum)
        if sum == targetSum:
            out.append(l_value)
            out.append(r_value)
            break
        elif sum < targetSum:
            l_index+=1
        elif sum > targetSum:
            r_index-=1

    return out