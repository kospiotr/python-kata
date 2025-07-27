"""
Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.


A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For
instance, the numbers [1, 3, 4] form a subsequence of the array
[1, 2, 3, 4], and so do the numbers [2, 4]. Note
that a single number in an array and the array itself are both valid
subsequences of the array.

Sample Input
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

Sample Output
true
"""


# noinspection PyPep8Naming
def isValidSubsequence_sol_1(array, sequence):
    """
    Brute force solution
    """

    if len(array) < len(sequence):
        return False

    l_pointer = 0
    r_pointer = 0
    s_pointer = 0

    print(array, sequence)

    def arr_val_index(from_index, val):
        for i in range(from_index, len(array)):
            if array[i] == val:
                return i
        return -1


    while s_pointer < len(sequence):
        s_value = sequence[s_pointer]
        r_pointer = arr_val_index(r_pointer, s_value)
        # print((r_pointer), (s_pointer, s_value))
        if r_pointer == -1:
            break
        s_pointer+=1
        r_pointer+=1

        if s_pointer == len(sequence):
            return True

    return False

def isValidSubsequence_sol_2(array, sequence):
    """
    Single iteration
    """
    a_index = 0
    s_index = 0
    while a_index < len(array):

        a_value = array[a_index]
        s_value = sequence[s_index]
        print((a_index, a_value), (s_index, s_value))

        if a_value == s_value:
            s_index+=1

        a_index+=1
        if s_index == len(sequence):
            return True

    return False

def isValidSubsequence_sol_3(array, sequence):
    """
    Single iteration
    """
    s_index = 0
    for a_value in array:
        s_value = sequence[s_index]
        if a_value == s_value:
            s_index +=1
        if s_index == len(sequence):
            return True

    return False