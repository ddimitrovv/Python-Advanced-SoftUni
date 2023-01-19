# Write a program that reads a matrix from the console and finds the 2x2
# top-left submatrix with the biggest sum of its values.
# On first line you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.
# • Be aware of IndexError
# • If you find more than one max square, print the top - left one

import sys


def sum_submatrix(row, column, matrix):
    a = matrix[row][column]
    b = matrix[row + 1][column]
    c = matrix[row][column + 1]
    d = matrix[row + 1][column + 1]
    submatrix = []
    submatrix.append([a, c])
    submatrix.append([b, d])
    sum_submatrix = a + b + c + d
    return submatrix, sum_submatrix


rows, columns = [int(x) for x in input().split(', ')]

matrix = []
maximum_sum= - sys.maxsize
max_submatrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(rows - 1):
    for column in range(columns - 1):
        submatrix, x = sum_submatrix(row, column, matrix)
        if x > maximum_sum:
            maximum_sum = x
            max_submatrix = submatrix

for row in max_submatrix:
    print(*row, sep=' ')
print(maximum_sum)
