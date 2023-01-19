# Write a program that reads a matrix from the console and changes its values. On the first line,
# you will get the matrix's rows - N. You will get elements for each column on the following N lines,
# separated with a single space. You will be receiving commands in the following format:
#     • "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
#     • "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.

def check_coordinates(row, col, size):
    return row in range(size) and col in range(size)


matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

while True:
    info = input()
    if info == 'END':
        break
    info = info.split()
    command = info[0]
    row = int(info[1])
    col = int(info[2])
    value = int(info[3])

    if check_coordinates(row, col, matrix_size):
        if command == 'Add':
            matrix[row][col] += value
        if command == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for row in matrix:
    print(*row, sep=' ')
