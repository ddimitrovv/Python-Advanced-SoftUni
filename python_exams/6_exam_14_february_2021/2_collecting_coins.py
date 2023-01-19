# You are playing a game, and your goal is to collect 100 coins.
# On the first line, you will be given a number representing the size of the field with a square shape.
# On the following few lines, you will be given the field with:
#     • One player - randomly placed in it and marked with the symbol "P"
#     • Numbers for coins placed at different positions of the field
#     • Walls marked with "X"
# After the field state, you will be given commands for the player's movement.
# Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it.
# The player moves in the given direction with one step for each command and collects all the coins that come across.
# If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
# Note: He can go through the same path many times, but he can collect the coins just once (the first time).
# There are only two possible outcomes of the game:
#     • The player hits a wall, loses the game, and his coins are reduced to 50%
#       and rounded down to the next-lowest number.
#     • The player collects at least 100 coins and wins the game.
# For more clarifications, see the examples below.
# Input
#     • A number representing the size of the field (matrix NxN)
#     • A matrix representing the field (each position separated by a single space)
#     • On each of the following lines, you will get a move command.
# Output
#     • If the player won the game, print: "You won! You've collected {total_coins} coins."
#     • If the player loses the game, print: "Game over! You've collected {total_coins} coins."
#     • Collected coins have to be rounded down to the next-lowest number.
#     • The player's path as coordinates in lists on separate lines:
# "Your path:
# [{row_position1}, {column_position1}]
# [{row_position2}, {column_position2}]
# …
# [{row_positionN}, {column_positionN}]"
# Constrains
#     • There will be no case in which less than 100 coins will be in the field
#     • All given numbers will be valid integers in the range [0, 100]
import math

field_size = int(input())

player_row = 0
player_col = 0

field = []
for i in range(field_size):
    new_row = input().split()
    for ch in new_row:
        if ch == 'P':
            player_row = i
            player_col = new_row.index(ch)
    field.append(new_row)


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

coins = 0
player_path = [[player_row, player_col],]

while coins < 100:
    direction = input()

    new_row, new_col = directions[direction](player_row, player_col)

    if new_row >= field_size:
        new_row = 0
    if new_row < 0:
        new_row = field_size - 1
    if new_col >= field_size:
        new_col = 0
    if new_col < 0:
        new_col = field_size - 1

    if field[new_row][new_col] == 'X':
        player_path.append([new_row, new_col])
        coins = math.floor(coins / 2)
        break
    if field[new_row][new_col].isdigit():
        coins += int(field[new_row][new_col])

    field[player_row][player_col] = '.'
    player_row, player_col = new_row, new_col
    field[player_row][player_col] = 'P'
    player_path.append([player_row, player_col])

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print('Your path:')
for positon in player_path:
    print(positon)
