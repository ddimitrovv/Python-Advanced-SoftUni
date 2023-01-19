# Two players bare-handedly throw small sharp-pointed missiles known as darts at a round target
# known as a dartboard. Who is going to win this game?
# You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
# 1   2   3   4   5   6   7
# 24  D   D   D   D   D   8
# 23  D   T   T   T   D   9
# 22  D   T   B   T   D   10
# 21  D   T   T   T   D   11
# 20  D   D   D   D   D   12
# 19  18  17  16  15  14  13
#
# Each of the two players starts with a score of 501, and they take turns to throw a dart – one throw for each player.
# The score for each turn is deducted from the player’s total score.
# The first player who reduces their score to zero or less wins the game.
# You are going to receive the information for every throw on a separate line.
# The coordinate information of a hit will be in the format: "({row}, {column})".
#     • If a player hits outside the dartboard, he does not score any points.
#     • If a player hits a number, it is deducted from his total.
#     • If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled
#       and then deducted from his total.
#     • If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled
#       and then deducted from his total.
#     • "B" is the bullseye. If a player hits it, he wins the game, and the program ends.
# For example, if Peter hits position with coordinates (2, 1),
# he wins (23 + 2 + 9 + 18) * 2 = 104 points, and they are deducted from his total.
# Your job is to find who won the game and with how many turns.
# Input
#     • The name of the first player and the name of the second player, separated by ", "
#     • 7 lines – the dartboard (separated by single space)
#     • On the next lines - the coordinates in the format: "({row}, {column})"
# Output
#     • You should print only one line containing the winner and his count of throws:
# "{name} won the game with {count_turns} throws!"
# Constrains
#     • There will always be exactly 7 lines
#     • There will always be a winner
#     • The points will be in range [1, 24]
#     • The coordinates will be in range [0, 100]
def sum_from_shot(r, c, matrix):
    return int(matrix[0][c]) + int(matrix[6][c]) + int(matrix[r][0]) + int(matrix[r][6])


first_player, second_player = input().split(', ')
dartboard = [input().split() for _ in range(7)]

players = {
    first_player: 501,
    second_player: 501,
}

trows = {
    first_player: 0,
    second_player: 0,
}

counter = 0
winner = ''
while True:
    player = first_player if counter % 2 == 0 else second_player
    row, col = [int(x) for x in input().strip('(').strip(')').split(', ')]
    trows[player] += 1
    if row in range(7) and col in range(7):
        if dartboard[row][col].isdigit():
            players[player] -= int(dartboard[row][col])
        elif dartboard[row][col] == 'T':
            players[player] -= sum_from_shot(row, col, dartboard) * 3
        elif dartboard[row][col] == 'D':
            players[player] -= sum_from_shot(row, col, dartboard) * 2
        elif dartboard[row][col] == 'B':
            winner = player
            break
    if players[player] <= 0:
        winner = player
        break
    counter += 1

print(f'{winner} won the game with {trows[winner]} throws!')
