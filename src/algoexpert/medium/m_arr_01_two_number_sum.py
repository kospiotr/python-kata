"""
Difficulty: Medium
Category: Arrays
Three Number Sum

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. The function should find all triplets in
the array that sum up to the target sum and return a two-dimensional array of
all these triplets. The numbers in each triplet should be ordered in ascending
order, and the triplets themselves should be ordered in ascending order with
respect to the numbers they hold.


If no three numbers sum up to the target sum, the function should return an
empty array.

Sample Input
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

Hints

Hint 1
Using three for loops to calculate the sums of all possible triplets in the array would generate an algorithm that runs in O(n^3) time, where n is the length of the input array. Can you come up with something faster using only two for loops?

Hint 2

Try sorting the array and traversing it once. At each number, place a left pointer on the number immediately to the right of your current number and a right pointer on the final number in the array. Check if the current number, the left number, and the right number sum up to the target sum. How can you proceed from there, remembering the fact that you sorted the array?

Hint 3

Since the array is now sorted (see Hint #2), you know that moving the left pointer mentioned in Hint #2 one place to the right will lead to a greater left number and thus a greater sum. Similarly, you know that moving the right pointer one place to the left will lead to a smaller right number and thus a smaller sum. This means that, depending on the size of each triplet's (current number, left number, right number) sum relative to the target sum, you should either move the left pointer, the right pointer, or both to obtain a potentially valid triplet.
Optimal Space & Time ComplexityO(n^2) time | O(n) space - where n is the length of the input array
"""


# noinspection PyPep8Naming
def threeNumberSum_sol_1(array, targetSum):

    # brute force method
    print()
    out = []
    if len(array) < 3:
        return out

    array.sort()
    for l_pointer in range(0, len(array)-2):
        for m_pointer in range(l_pointer+1, len(array)-1):
            for r_pointer in range(m_pointer+1, len(array)):
                l_value = array[l_pointer]
                m_value = array[m_pointer]
                r_value = array[r_pointer]
                sum = l_value + m_value + r_value

                if sum == targetSum:
                    out.append([l_value, m_value, r_value])

    return out

def threeNumberSum_sol_2(array, targetSum):

    # sliding pointers, assuming there are no duplicates
    # when there are duplicates only brute force method works correctly
    print(targetSum)
    out = []

    array.sort()

    l_pointer = 0
    while l_pointer < len(array) - 2:
        m_pointer = l_pointer + 1
        r_pointer = len(array) - 1

        while m_pointer < r_pointer:
            l_value = array[l_pointer]
            m_value = array[m_pointer]
            r_value = array[r_pointer]

            sum = l_value + m_value + r_value
            print((l_pointer, l_value),(m_pointer, m_value), (r_pointer, r_value), sum)

            if sum == targetSum:
                out.append([l_value, m_value, r_value])
                m_pointer+=1
                r_pointer-=1

            if sum < targetSum:
                m_pointer+=1

            if sum > targetSum:
                r_pointer-=1

        l_pointer+=1

    return out