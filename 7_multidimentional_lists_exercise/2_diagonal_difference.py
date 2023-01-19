# Write a program that finds the difference between the sums
# of the square matrix diagonals (absolute value).
#
# On the first line, you will receive an integer N - the size of a square matrix.
# The following N lines hold the values for each column - N numbers separated by a single space.
# Print the absolute difference between the primary and the secondary diagonal sums.

matrix_size = int(input())

matrix = []
primary_diagonal = list()
secondary_diagonal = list()

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

for i in range(matrix_size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][matrix_size - i - 1])

print(f'{abs(sum(primary_diagonal) - sum(secondary_diagonal))}')
