# You are visiting Santa Claus' workshop, and it is complete chaos.
# You will need to help Santa find all items scattered around the workshop.
# You will be given the size of the matrix in the format "{rows}, {columns}".
# It is the Santa's workshop represented as some symbols separated by a single space:
#     • Your position is marked with the symbol "Y"
#     • Christmas decorations are marked with the symbol "D"
#     • Gifts are marked with the symbol "G"
#     • Cookies are marked with the symbol "C"
#     • All the empty positions will be marked with "."
# After the field state, you will be given commands until you receive the command "End".
# The commands will be in the format "right/left/up/down-{steps}".
# You should move in the given direction with the given steps and collect all the items that come across.
# If you go out of the field, you should continue to traverse the field from the opposite side
# in the same direction. You should mark your path with "x".
# Your current position should always be marked with "Y".
# Keep track of all collected items. If you've collected all items at any point,
# end the program and print: "Merry Christmas!".
# Input
#     • On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
#     • On the next lines, you will receive each row with its columns - symbols, separated by a single space.
#     • On the following lines, you will receive commands in the format described above
#       until you receive the command "End" or until you collect all items.
# Output
#     • On the first line, if you have collected all items, print:
#         ◦ "Merry Christmas!"
#         ◦ Otherwise, skip the line
#     • Next, print the number of collected items in the format:
#         ◦ "You've collected:
#         ◦ - {number_of_decoration} Christmas decorations
#         ◦ - {number_of_gifts} Gifts
#         ◦ - {number_of_cookies} Cookies"
#     • Finally, print the field, as shown in the examples.
# Constrains
#     • All the commands will be valid
#     • There will always be at least one item
#     • The dimensions of the matrix will be integers in the range [1, 20]
#     • The field will always have only one "Y"
#     • On the field, there will always be only the symbols shown above.

rows, columns = [int(x) for x in input().split(', ')]

santa_workshop = []
santa_row = 0
santa_col = 0
total_items = -1

for row in range(rows):
    new_row_content = input().split()
    for ch in new_row_content:
        if ch == 'Y':
            santa_row = row
            santa_col = new_row_content.index(ch)
        if ch != ".":
            total_items += 1

    santa_workshop.append(new_row_content)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

collectable_items = {
    'Christmas decorations': 0,
    'Gifts': 0,
    'Cookies': 0,
}

while True:
    if total_items == 0:
        break
    command = input()
    if command == 'End':
        break

    santa_workshop[santa_row][santa_col] = 'Y'
    direction, steps = command.split('-')
    steps = int(steps)

    for i in range(steps):
        new_row, new_col = directions[direction](santa_row, santa_col)
        if new_row >= rows:
            new_row = 0
        if new_row < 0:
            new_row = rows - 1
        if new_col >= columns:
            new_col = 0
        if new_col < 0:
            new_col = columns - 1

        if santa_workshop[new_row][new_col] != '.' and santa_workshop[new_row][new_col] != 'x':

            if santa_workshop[new_row][new_col] == 'D':
                collectable_items['Christmas decorations'] += 1
            if santa_workshop[new_row][new_col] == 'G':
                collectable_items['Gifts'] += 1
            if santa_workshop[new_row][new_col] == 'C':
                collectable_items['Cookies'] += 1
            total_items -= 1

        santa_workshop[santa_row][santa_col] = 'x'
        santa_row, santa_col = new_row, new_col
        santa_workshop[santa_row][santa_col] = 'Y'

        if total_items == 0:
            break


if total_items == 0:
    print('Merry Christmas!')
print("You've collected:")
for item, value in collectable_items.items():
    print(f'- {value} {item}')
for row in santa_workshop:
    print(*row, sep=' ')
