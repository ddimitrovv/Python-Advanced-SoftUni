# Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
# You will receive a 6x6 field on separate lines with:
#     • One rover - marked with the letter "E"
#     • Water deposit (one or many) - marked with the letter "W"
#     • Metal deposit (one or many) - marked with the letter "M"
#     • Concrete deposit (one or many) - marked with the letter "C"
#     • Rock (one or many) - marked with the letter "R"
#     • Empty positions will be marked with "-"
# After that, you will be given the commands for the rover's movement
# on one line separated by a comma and a space (", "). Commands can be: "up", "down", "left", or "right".
# For each command, the rover moves in the given directions with one step,
# and it can land on one of the given types of deposit or a rock:
#     • When it lands on a deposit, you must print the coordinates of that deposit
#       in the format shown below and increase its value by 1.
#     • If the rover lands on a rock, it gets broken.
#       Print the coordinates where it got broken in the format shown below, and the program ends.
#     • If the rover goes out of the field, it should continue from the opposite side in the same direction.
#       Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix),
#       it should be placed at position (3, 5).
# The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
# Stop the program if you run out of commands or the rover gets broken.
# Input
#     • On the first 6 lines, you will receive the matrix.
#     • On the following line, you will receive the commands for the rover separated by a comma and a space.
# Output
#     • For each deposit found while you go through the commands,
#       print out on the console: "{Water, Metal or Concrete} deposit found at ({row}, {col})"
#     • If the rover hits a rock, print the coordinates where it got broken in the format:
#       "Rover got broken at ({row}, {col})"
# After you go through all the commands or the rover gets broken, print out on the console:
#     • If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
#     • Otherwise, print on the console: "Area not suitable to start the colony."

field_size = 6

matrix = []
rover_row = 0
rover_col = 0
deposits = {}
for i in range(field_size):
    new_row = [x for x in input().split()]
    for ch in new_row:
        if ch == 'E':
            rover_row = i
            rover_col = new_row.index(ch)
        if ch != 'E' and ch != '-' and ch != 'R':
            if ch not in deposits.keys():
                deposits[ch] = 0

    matrix.append(new_row)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

commands = [x for x in input().split(', ')]

matrix[rover_row][rover_col] = '-'
for direction in commands:

    new_row, new_col = directions[direction](rover_row, rover_col)
    if new_row >= field_size:
        new_row = 0
    if new_row < 0:
        new_row = field_size - 1
    if new_col >= field_size:
        new_col = 0
    if new_col < 0:
        new_col = field_size - 1

    if matrix[new_row][new_col] == 'R':
        print(f'Rover got broken at ({new_row}, {new_col})')
        break

    if matrix[new_row][new_col] in deposits.keys():
        deposits[matrix[new_row][new_col]] += 1

        if matrix[new_row][new_col] == 'W':
            print(f'Water deposit found at ({new_row}, {new_col})')

        if matrix[new_row][new_col] == 'C':
            print(f'Concrete deposit found at ({new_row}, {new_col})')

        if matrix[new_row][new_col] == 'M':
            print(f'Metal deposit found at ({new_row}, {new_col})')

    matrix[new_row][new_col] = '-'
    rover_row, rover_col = new_row, new_col

for key, value in deposits.items():
    if value == 0:
        print('Area not suitable to start the colony.')
        break
else:
    print('Area suitable to start the colony.')
