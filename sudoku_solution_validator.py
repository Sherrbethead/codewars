"""
Description

Sudoku Background:
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells
of the grid with digits from 1 to 9, so that each column, each row, and each of
the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1
to 9.
More info at: http://en.wikipedia.org/wiki/Sudoku
Sudoku Solution Validator:
Write a function validSolution/ValidateSolution/valid_solution() that accepts a
2D array representing a Sudoku board, and returns true if it is a valid
solution, or false otherwise. The cells of the sudoku board may also contain
0's, which will represent empty cells. Boards containing one or more zeroes are
considered to be invalid solutions.
The board is always 9 cells by 9 cells, and every cell only contains integers
from 0 to 9.
"""


def valid_solution(board):
    sum_rows = [sum(i) for i in board]
    sum_cols = [sum(j) for j in zip(*board)]
    sums_qrs1 = [sum(k) for k in zip(*board[:3])]
    sums_qrs2 = [sum(k) for k in zip(*board[3:6])]
    sums_qrs3 = [sum(k) for k in zip(*board[6:])]
    sums_qrs = [sum(sums_qrs1[:3]), sum(sums_qrs1[3:6]), sum(sums_qrs1[6:]),
                sum(sums_qrs2[:3]), sum(sums_qrs2[3:6]), sum(sums_qrs2[6:]),
                sum(sums_qrs3[:3]), sum(sums_qrs3[3:6]), sum(sums_qrs3[6:])]
    return sum_rows.count(45) == sum_cols.count(45) == sums_qrs.count(45) == 9


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]))  # True
print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 0, 3, 4, 9],
                     [1, 0, 0, 3, 4, 2, 5, 6, 0],
                     [8, 5, 9, 7, 6, 1, 0, 2, 0],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 0, 1, 5, 3, 7, 2, 1, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 0, 0, 4, 8, 1, 1, 7, 9]]))  # False
