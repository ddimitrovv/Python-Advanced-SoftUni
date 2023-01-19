# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move.
# On the second line, you will receive the commands for the miner's movement,
# separated by a single space. The possible commands are "left", "right", "up" and "down".
# In the end, you will receive each row of the field on a separate line.
# The possible characters that may appear on the screen are:
#     • * - a regular position on the field
#     • e - the end of the route
#     • c - coal
#     • s - miner
# The miner starts moving from the position "s". He should perform the given commands successively,
# moving with only one position in the given direction.
# If the miner has reached the edge of the field and the following command
# indicates that he has to get out of the area, he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*".
# Keep track of the collected coal. In the end, you should print
# whether the miner has succeeded in collecting the coal or not and his final position:
#     • If the miner has collected all coal in the field, the program stops,
#       and you should print the message: "You collected all coal! ({row_index}, {col_index})".
#     • If the miner steps at "e", the game is over (the program stops),
#       and you should print the message: "Game over! ({row_index}, {col_index})".
#     • If there are no more commands and none of the above cases had happened,
#       you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
#     • Field size - an integer number
#     • Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
#     • The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
#     • There are three types of output as mentioned above.
# Constraints
#     • The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
#     • The field will always have only one "s"

from collections import deque


field_size = int(input())
commands = deque(input().split())
field = []
coal = 0
miner_row = 0
miner_col = 0

for row in range(field_size):
    new_row = input().split()
    field.append(new_row)
    for col in range(field_size):
        if new_row[col] == 'c':
            coal += 1
        if new_row[col] == 's':
            miner_row = row
            miner_col = col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

end_of_road = False
while coal and commands:

    field[miner_row][miner_col] = '*'
    direction = commands.popleft()

    next_row, next_col = directions[direction](miner_row, miner_col)
    if next_row not in range(len(field)) or next_col not in range(len(field[0])):
        continue

    miner_row, miner_col = next_row, next_col

    if field[miner_row][miner_col] == '*':
        continue
    if field[miner_row][miner_col] == 'e':
        print(f'Game over! ({miner_row}, {miner_col})')
        end_of_road = True
        break
    if field[miner_row][miner_col] == 'c':
        coal -= 1

if not end_of_road:
    if coal > 0:
        print(f'{coal} pieces of coal left. ({miner_row}, {miner_col})')
    else:
        print(f'You collected all coal! ({miner_row}, {miner_col})')
