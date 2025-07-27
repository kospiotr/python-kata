"""
Difficulty: Easy
Category: Arrays
Transpose Matrix

You're given a 2D array of integers matrix. Write a function
that returns the transpose of the matrix.

The transpose of a matrix is a flipped version of the original matrix across
its main diagonal (which runs from top-left to bottom-right); it switches
the row and column indices of the original matrix.

You can assume the input matrix always has at least 1 value; however its
width and height are not necessarily the same.

Sample Input #1
matrix = [
[1, 2],
]
Sample Output # 1
[
[1],
[2]
]

Sample Input #2
matrix = [
[1, 2],
[3, 4],
[5, 6]
]
Sample Output #2
[
[1, 3, 5],
[2, 4, 6]
]

Sample Input #3
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Sample Output #3
[
[1, 4, 7],
[2, 5, 8],
[3, 6, 9]
]
HintsHint 1
The row and column indices of each entry in the matrix should be flipped.
For example, the value at matrix[1][2] will be at
matrix[2][1] in the transpose of the matrix.

Hint 2

Each column in the matrix should be become a row in the transpose of the
matrix. Each row in the matrix should become a column in the transpose
of the matrix.

Hint 3

Try iterating one column at a time, and with each column, create a row of the
values to add to the transpose of the matrix.
Optimal Space & Time ComplexityO(w * h) time | O(w * h) space - where w is the width of the matrix and h is the height
"""

def transposeMatrix_sol_1(matrix):
    out = []
    for row_index, row_value in enumerate(matrix):
        for column_index, cell_value in enumerate(matrix[row_index]):
            new_row_index = column_index
            new_col_index = row_index
            if new_col_index == 0:
                out.append([])
            out[new_row_index].append(cell_value)
            # print('R:', new_row_index, 'C:',new_col_index, cell_value)
    # print(out)
    return out