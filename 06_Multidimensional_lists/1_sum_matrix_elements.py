# Write a program that reads a matrix from the console and prints:
#     • The sum of all numbers in the matrix
#     • The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".

n, m = [int(x) for x in input().split(', ')]

matrix = list()
matrix_sum = 0

for _ in range(n):
    new_row = [int(x) for x in input().split(', ')]
    matrix.append(new_row)
    matrix_sum += sum(new_row)

print(matrix_sum)
print(matrix)
