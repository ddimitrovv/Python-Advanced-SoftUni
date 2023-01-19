# Everybody remembers the old snake game. Now it is time to create your own.
#
# You will be given an integer n for the size of the snake territory with square shape. On the next n lines,
# you will receive the rows of the territory. The snake will be placed on a random position,
# marked with the letter 'S'. On random positions there will be food, marked with '*'.
# There might also be a lair on the territory. The lair has two burrows. They are marked with the letter - 'B'.
# All the empty positions will be marked with '-'.
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside a burrow, it goes out on the position of the other burrow and then both burrows disappear.
# If the snake goes out of its territory, it loses, can't return and the program ends.
# The snake needs at least 10 food quantity to win.
# When the snake has gone outside its territory or has eaten enough food, the game ends.
# Input
#     • On the first line, you are given the integer n – the size of the square matrix.
#     • The next n lines holds the values for every row.
#     • On each of the next lines you will get a move command.
# Output
#     • On the first line:
#         ◦ If the snake goes out of its territory, print: "Game over!"
#         ◦ If the snake eat enough food, print: "You won! You fed the snake."
#     • On the second line print all food eaten: "Food eaten: {food quantity}"
#     • In the end print the matrix.
# Constraints
#     • The size of the square matrix will be between [2…10].
#     • There will always be 0 or 2 burrows, marked with - 'B'.
#     • The snake position will be marked with 'S'.
#     • The snake will always either go outside its territory or eat enough food.
#     • There will be no case in which the snake will go through itself.
def is_inside(row_check, col_check):
    return 0 <= row_check < field_size and 0 <= col_check < field_size


def burrow_move(burrows_set, prev_row, prev_col):
    burrow_row, burrow_col = 0, 0
    for positions in burrows_set:
        if (prev_row, prev_col) == positions:
            burrows_set.remove(positions)
        burrow_row, burrow_col = burrows_set[0][0], burrows_set[0][1]
    return burrow_row, burrow_col


field_size = int(input())

snake_field = []
snake_row = 0
snake_col = 0

burrows = list()
for row in range(field_size):
    new_row_content = [x for x in input()]
    for ch in new_row_content:
        if ch == 'S':
            snake_row = row
            snake_col = new_row_content.index(ch)
        if ch == 'B':
            burrows.append((row, new_row_content.index(ch)))

    snake_field.append(new_row_content)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

food_eaten = 0

while True:

    direction = input()

    new_row, new_col = directions[direction](snake_row, snake_col)
    if not is_inside(new_row, new_col):
        snake_field[snake_row][snake_col] = '.'
        break
    if snake_field[new_row][new_col] == 'B':
        snake_field[snake_row][snake_col] = '.'
        snake_field[new_row][new_col] = '.'
        snake_row, snake_col = burrow_move(burrows, new_row, new_col)
        snake_field[snake_row][snake_col] = 'S'
        continue
    if snake_field[new_row][new_col] == '*':
        food_eaten += 1

    snake_field[snake_row][snake_col] = '.'
    snake_row, snake_col = new_row, new_col
    snake_field[snake_row][snake_col] = 'S'
    if food_eaten == 10:
        break

if food_eaten > 9:
    print('You won! You fed the snake.')
else:
    print('Game over!')
print(f'Food eaten: {food_eaten}')
for row in snake_field:
    print(''.join(row))
