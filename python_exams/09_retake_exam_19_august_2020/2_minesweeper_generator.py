# Everybody remembers the old mines game. Now it is time to create your own.
#
# You will be given an integer n for the size of the mines field with square shape
# and another one for the number of bombs that you have to place in the field.
# On the next n lines, you will receive the position for each bomb.
# Your task is to create the game field placing the bombs at the correct positions and mark them with "*",
# and calculate the numbers in each cell of the field. Each cell represents a number
# of all bombs directly near it (up, down, left, right and the 4 diagonals).
# Input
#     • On the first line, you are given the integer n – the size of the square matrix.
#     • On the second line – the number of the bombs.
#     • The next n lines holds the position of each bomb.
# Output
#     • Print the matrix you've created.
# Constraints
#     • The size of the square matrix will be between [2…15].


def bombs_positions(row, col, matrix):
    counter = 0
    next_row, next_col = row - 1, col  # up
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1
    next_row, next_col = row - 1, col + 1  # up_right
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1
    next_row, next_col = row - 1, col - 1  # up_left
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1
    next_row, next_col = row, col + 1  # right
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1
    next_row, next_col = row, col - 1  # left
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1
    next_row, next_col = row + 1, col  # down
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1
    next_row, next_col = row + 1, col - 1  # down_right
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1
    next_row, next_col = row + 1, col + 1  # down_left
    if next_row in range(len(matrix)) and next_col in range(len(matrix)):
        if matrix[next_row][next_col] == '*':
            counter += 1

    return counter


matrix_size = int(input())
field = [[0 for x in range(matrix_size)] for i in range(matrix_size)]

number_of_bombs = int(input())

for _ in range(number_of_bombs):
    bomb_row, bomb_col = [int(x) for x in input().strip('(').strip(')').split(', ')]
    field[bomb_row][bomb_col] = '*'

    for current_row in range(len(field)):
        for current_col in range(len(field)):
            if field[current_row][current_col] != '*':
                field[current_row][current_col] = bombs_positions(current_row, current_col, field)


for line in field:
    print(*line, sep=' ')
