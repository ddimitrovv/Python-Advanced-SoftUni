# You will be given a string. Then, you will be given an integer N
# for the size of the field with square shape. On the next N lines,
# you will receive the rows of the field. The player will be placed on a random position,
# marked with "P". On random positions there will be letters.
# All the empty positions will be marked with "-".
# Each turn you will be given commands for the player’s movement.
# If he moves to a letter, he consumes it, concatenates it to the initial string
# and the letter disappears from the field. If he tries to move outside the field,
# he is punished - he loses the last letter in the string, if there are any,
# and the player’s position is not changed.
# At the end print all letters and the field.
# Input
#     • On the first line, you are given the initial string
#     • On the second line, you are given the integer N - the size of the square matrix
#     • The next N lines holds the values for every row
#     • On the next line you receive a number M
#     • On the next M lines you will get a move command
# Output
#     • On the first line the final state of the string
#     • In the end print the matrix
# Constraints
#     • The size of the square matrix will be between [2…10]
#     • The player position will be marked with "P"
#     • The letters on the field will be any letter except for "P"
#     • Move commands will be: "up", "down", "left", "right"

def is_inside(check_row, check_col, matrix):
    return check_row in range(len(matrix)) and check_col in range(len(matrix))


initial_string = input()
matrix_size = int(input())

field = []
player_row, player_col = 0, 0

for row in range(matrix_size):
    new_row = [x for x in input()]
    if 'P' in new_row:
        player_row = row
        player_col = new_row.index('P')
    field.append(new_row)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

number_of_commands = int(input())

for _ in range(number_of_commands):
    direction = input()
    new_row, new_col = directions[direction](player_row, player_col)

    if not is_inside(new_row, new_col, field):
        initial_string = initial_string[:-1]
    else:
        if field[new_row][new_col] != '-':
            initial_string += field[new_row][new_col]

        field[player_row][player_col] = '-'
        field[new_row][new_col] = 'P'
        player_row, player_col = new_row, new_col

print(initial_string)
for row in field:
    print(''.join(row))
