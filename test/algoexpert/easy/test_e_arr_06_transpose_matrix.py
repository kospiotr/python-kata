import pytest

from src.algoexpert.easy.e_arr_06_transpose_matrix import transposeMatrix_sol_1, transposeMatrix_sol_2

test_cases = [
    ([
         [1, 2]
     ], [
         [1],
         [2]
     ]),
    ([
         [1, 2],
         [3, 4],
         [5, 6]
     ],
     [
         [1, 3, 5],
         [2, 4, 6]
     ]
    ),
([[1]],[[1]]),
([[1],[-1]],[[1, -1]]),
([[1,2,3]],[[1], [2], [3]]),
([[1],[2],[3]],[[1, 2, 3]]),
([[1,2,3],[4,5,6]],[[1, 4], [2, 5], [3, 6]]),
([[0,0,0],[1,1,1]],[[0, 1], [0, 1], [0, 1]]),
([[0,1],[0,1],[0,1]],[[0, 0, 0], [1, 1, 1]]),
([[0,0,0],[0,0,0]],[[0, 0], [0, 0], [0, 0]] ),
([[1,4],[2,5],[3,6]],[[1, 2, 3], [4, 5, 6]]),
([[-7,-7],[100,12],[-33,17]],[[-7, 100, -33], [-7, 12, 17]]),
([[1,2,3],[4,5,6],[7,8,9]],[[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
([[1,4,7],[2,5,8],[3,6,9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
([[5,6,3,-3,12],[-3,6,5,2,-1],[0,0,3,12,3]],[[5, -3, 0], [6, 6, 0], [3, 5, 3], [-3, 2, 12], [12, -1, 3]]),
([[0,-1,-2,-3],[4,5,6,7],[2,3,-2,-3],[42,100,30,-42]],[[0, 4, 2, 42], [-1, 5, 3, 100], [-2, 6, -2, 30], [-3, 7, -3, -42]] ),
([[1234,6935,4205],[-23459,314159,0],[100,3,987654]],[[1234, -23459, 100], [6935, 314159, 3], [4205, 0, 987654]])
]


@pytest.mark.parametrize("matrix, result_expected", test_cases)
def test_transposeMatrix_sol_1(matrix, result_expected):
    assert transposeMatrix_sol_1(matrix) == result_expected

@pytest.mark.parametrize("matrix, result_expected", test_cases)
def test_transposeMatrix_sol_2(matrix, result_expected):
    assert transposeMatrix_sol_2(matrix) == result_expected
