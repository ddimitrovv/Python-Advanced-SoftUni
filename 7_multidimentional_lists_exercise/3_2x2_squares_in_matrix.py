# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
# On the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.

def is_identical_chars(row, column, matrix):
    a = matrix[row][column]
    b = matrix[row + 1][column]
    c = matrix[row][column + 1]
    d = matrix[row + 1][column + 1]
    return a == b == c == d


rows, columns = [int(x) for x in input().split()]

matrix = []
squares_number = 0

for _ in range(rows):
    matrix.append([x for x in input().split()])

for row in range(rows - 1):
    for column in range(columns - 1):
        if is_identical_chars(row, column, matrix):
            squares_number += 1

print(squares_number)
