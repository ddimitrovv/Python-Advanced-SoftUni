# Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data.
# Your program should receive commands in the format:
# "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are
# the coordinates of two points in the matrix.
# A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less),
# separated by a single space.
#     • If the command is valid, you should swap the values at the given indexes and print the matrix
#       at each step (thus, you will be able to check if the operation was performed correctly).
#     • If the command is not valid (does not contain the keyword "swap",
#       has fewer or more coordinates entered, or the given coordinates are not valid),
#       print "Invalid input!" and move on to the following command.
#       A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.

def check_indices(first, second, third, fourth, rows, columns):
    return first in range(rows) and second in range(columns) and third in range(rows) and fourth in range(columns)


rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == 'END':
        break
    info = command.split()

    if info[0] != 'swap' and len(info) != 5:
        print('Invalid input!')
        continue
    if not info[1].isdigit() or not info[2].isdigit() or not info[3].isdigit() or not info[4].isdigit():
        print('Invalid input!')
        continue
    else:
        first = int(info[1])
        second = int(info[2])
        third = int(info[3])
        fourth = int(info[4])
        if check_indices(first, second, third, fourth, rows, columns):
            matrix[first][second], matrix[third][fourth] = matrix[third][fourth], matrix[first][second]
            for row in matrix:
                print(*row, sep=' ')
        else:
            print('Invalid input!')
            continue
