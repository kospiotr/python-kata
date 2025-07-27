"""
Write a function that takes in a non-empty array of integers that are sorted
in ascending order and returns a new array of the same length with the squares
of the original integers also sorted in ascending order.

Sample Input
array = [1, 2, 3, 5, 6, 8, 9]

Sample Output
[1, 4, 9, 25, 36, 64, 81]
"""

def sortedSquaredArray_sol_1(array):
    # Write your code here.
    out = list([el * el for el in array])
    out.sort()
    return out

def sortedSquaredArray_sol_2(array):
    out = [None] * len(array)
    l_index = 0
    r_index = len(array) - 1
    o_index = len(array) - 1
    while l_index <= r_index:
        l_abs_value = abs(array[l_index])
        r_abs_value = abs(array[r_index])

        if l_abs_value < r_abs_value:
            out[o_index]=r_abs_value * r_abs_value
            o_index-=1
            r_index-=1

        else:
            out[o_index]=l_abs_value * l_abs_value
            o_index-=1
            l_index+=1

        print((l_index, l_abs_value), (r_index, r_abs_value), out)

    return out
