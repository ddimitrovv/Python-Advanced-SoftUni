# Alice is going to the mad tea party, to see her friends.
# On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape.
# On the following n lines, you will receive the rows of the territory:
#     • Alice will be placed in a random position, marked with the letter "A".
#     • On the territory, there will be bags of tea, represented as numbers.
#       If Alice steps on a number position, she collects the tea bags
#       and increases the quantity with the corresponding number.
#     • There will always be one rabbit hole on the territory marked with the letter "R".
#     • All the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements.
# Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party,
# and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole
# or goes out of the territory, she can't return, and the program ends.
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
#     • On the first line, you will be given the integer n – the size of the square matrix
#     • On the following n lines - matrix representing the field (each position separated by a single space)
#     • On each of the following lines, you will be given a move command
# Output
#     • On the first line:
#         ◦ If Alice steps on the rabbit hole, or she goes out of the territory, print:
# "Alice didn't make it to the tea party."
#         ◦ If she collected at least 10 bags of tea, print:
# "She did it! She went to the party."
#     • On the following lines, print the matrix.
# Constraints
#     • Alice will always either go outside the Wonderland or collect 10 bags of tea
#     • All the commands will be valid
#     • All the given numbers will be valid integers in the range [0, 10]

field_size = int(input())

field = []
alice_row = 0
alice_col = 0
for row in range(field_size):
    new_row = [x for x in input().split()]
    for ch in new_row:
        if ch == 'A':
            alice_row = row
            alice_col = new_row.index(ch)
    field.append(new_row)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

tea_bags = 0

while tea_bags < 10:
    field[alice_row][alice_col] = '*'
    direction = input()

    next_row, next_col = directions[direction](alice_row, alice_col)
    if next_row not in range(field_size) or next_col not in range(field_size):
        break
    alice_row, alice_col = next_row, next_col
    if field[alice_row][alice_col] == '.' or field[alice_row][alice_col] == '*':
        continue
    if field[alice_row][alice_col] == 'R':
        break
    tea_bags += int(field[alice_row][alice_col])

field[alice_row][alice_col] = '*'
if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
for row in field:
    print(*row, sep=' ')
