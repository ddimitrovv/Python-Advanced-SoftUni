# Write a program that reads a matrix from the console
# and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.

n, m = [int(x) for x in input().split(', ')]

matrix = list()

for _ in range(n):
    matrix.append([int(x) for x in input().split()])
sum_column = [0] * m
for row_index in range(n):
    for column_index in range(m):
        sum_column[column_index] += matrix[row_index][column_index]

print(*sum_column, sep='\n')
