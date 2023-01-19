# Your task is to collect as many eggs as possible.
# On the first line, you will be given a number representing the size of the field.
# On the following few lines, you will be given a field with:
#     • One bunny - randomly placed in it and marked with the symbol "B"
#     • Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some directions, you should not consider
# the fields after the trap in this direction. For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
#     • A number representing the size of the field
#     • The matrix representing the field (each position separated by a single space)
# Output
#     • The direction which should be considered as best (lowercase)
#     • The field positions from which we are collecting eggs as lists
#     • The total number of eggs collected
# Constraints
#     • There will NOT be two or more paths consisting of the same total amount of eggs.

import sys

field_size = int(input())

field = []
bunny_row = 0
bunny_col = 0
for row in range(field_size):
    new_row = [x for x in input().split()]
    for ch in new_row:
        if ch == 'B':
            bunny_row = row
            bunny_col = new_row.index(ch)
    field.append(new_row)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

max_sum = -sys.maxsize
best_direction = ''
best_direction_coordinates = []
for direction in directions:
    current_sum = 0
    current_coordinates = []
    row, col = directions[direction](bunny_row, bunny_col)
    while row in range(field_size) and col in range(field_size) and field[row][col] != 'X':
        current_sum += int(field[row][col])
        current_coordinates.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > max_sum and current_coordinates:
        max_sum = current_sum
        best_direction = direction
        best_direction_coordinates = current_coordinates

print(best_direction)
print(*best_direction_coordinates, sep='\n')
print(max_sum)
