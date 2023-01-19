# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns.
# It is a shotgun range represented as some symbols separated by a single space:
#     • Your position is marked with the symbol "A"
#     • Targets marked with symbol "x"
#     • All the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive.
# The possible commands are:
#     • "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
#       You can only move if the field you want to step on is marked with ".".
#     • "shoot {right/left/up/down}" – you should shoot in the given direction
#       (from your current position without moving). Beware that there might be targets that stand
#       in the way of other targets, and you cannot reach them - you can shoot only the nearest target.
#       When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
#     • If at any point there are no targets left, end the program and print:
#       "Training completed! All {count_targets} targets hit.".
#     • If, after you perform all the commands, there are some targets left print:
#       "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
#     • 5 lines representing the field (symbols, separated by a single space)
#     • N - count of commands
#     • On the following N lines - the commands in the format described above
# Output
#     • On the first line, print one of the following:
#         ◦ If all the targets were shot
# "Training completed! All {count_targets} targets hit."
#         ◦ Otherwise:
#               	       "Training not completed! {count_left_targets} targets left."
#     • Finally, print the index positions "[{row}, {column}]" of the targets that you hit.
# Constrains
#     • All the commands will be valid
#     • There will always be at least one target

battle_field = []

player_row = 0
player_col = 0
targets = []
for row in range(5):
    new_row = [x for x in input().split()]
    for ch in new_row:
        if ch == 'A':
            player_row = row
            player_col = new_row.index(ch)
        if ch == 'x':
            targets.append([row, new_row.index(ch)])
    battle_field.append(new_row)

number_of_commands = int(input())

directions = {
    'right': lambda r, c, x: (r, c + x),
    'left': lambda r, c, x: (r, c - x),
    'up': lambda r, c, x: (r - x, c),
    'down': lambda r, c, x: (r + x, c),
}
hitted_targets = []
for _ in range(number_of_commands):

    command = input().split()
    action = command[0]
    direction = command[1]

    if action == 'move':
        next_row, next_col = directions[direction](player_row, player_col, int(command[2]))

        if next_row not in range(len(battle_field)) or next_col not in range(len(battle_field[0])) or \
                battle_field[next_row][next_col] == 'x':
            continue

        battle_field[player_row][player_col] = '.'
        battle_field[next_row][next_col] = 'A'
        player_row, player_col = next_row, next_col

    if action == 'shoot':

        for i in range(len(battle_field) - 1):
            next_row, next_col = directions[direction](player_row, player_col, i)
            if next_row not in range(len(battle_field)) or next_col not in range(len(battle_field[0])):
                break
            if battle_field[next_row][next_col] == 'x':
                hitted_targets.append([next_row, next_col])
                battle_field[next_row][next_col] = '.'
                break

    if len(targets) == len(hitted_targets):
        break

if len(targets) == len(hitted_targets):
    print(f'Training completed! All {len(targets)} targets hit.')
else:
    print(f'Training not completed! {len(targets) - len(hitted_targets)} targets left.')
if hitted_targets:
    for target in hitted_targets:
        print(target)
