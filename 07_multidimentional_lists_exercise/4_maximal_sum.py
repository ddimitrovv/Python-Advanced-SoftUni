# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square
# with a maximum sum of its elements. There will be no case with two or more 3x3 squares
# with equal maximal sum.
# Input
#     • On the first line, you will receive the rows and columns in the format "{rows} {columns}" –
#       integers in the range [1, 20]
#     • On the following lines, you will receive each row with its columns -
#       integers, separated by a single space in the range [-20, 20]
# Output
#     • On the first line, print the maximum sum of the elements in the 3x3 square
#       in the format "Sum = {sum}"
#     • On the following 3 lines, print each element of the found submatrix,
#       separated by a single space

import sys


def sum_submatrix(row, column, matrix):
    a = matrix[row][column]
    b = matrix[row][column + 1]
    c = matrix[row][column + 2]
    d = matrix[row + 1][column]
    e = matrix[row + 1][column + 1]
    f = matrix[row + 1][column + 2]
    g = matrix[row + 2][column]
    h = matrix[row + 2][column + 1]
    j = matrix[row + 2][column + 2]
    submatrix = []
    submatrix.append([a, b, c])
    submatrix.append([d, e, f])
    submatrix.append([g, h, j])
    sum_submatrix = a + b + c + d + e + f + g + h + j
    return submatrix, sum_submatrix

rows, columns = [int(x) for x in input().split()]

matrix = []
maximum_sum = -sys.maxsize
max_submatrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for column in range(columns - 2):
        submatrix, x = sum_submatrix(row, column, matrix)
        if x > maximum_sum:
            maximum_sum = x
            max_submatrix = submatrix

print(f"Sum = {maximum_sum}")
for row in range(len(max_submatrix)):
    print(f"{' '.join(str(x) for x in max_submatrix[row])}")
