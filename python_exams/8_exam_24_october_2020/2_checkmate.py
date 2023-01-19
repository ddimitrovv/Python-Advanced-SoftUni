# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
#     • "." – empty square
#     • "Q" – a queen
#     • "K" – the king
# Your job is to find which queens can capture the king and print them.
# The moves that the queen can do is to move diagonally,
# horizontally and vertically (basically all the moves that all the other figures can do except from the knight).
# Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king.
# For more clarification see the examples.
# Input
#     • 8 lines – the state of the board (each square separated by single space)
# Output
#     • The positions of the queens that can capture the king as lists
#     • If the king cannot be captured, print: "The king is safe!"
#     • The order of output does not matter
# Constrains
#     • There will always be exactly 8 lines
#     • There will always be exactly one King
#     • Only the 3 symbols described above will be present in the input
def diagonals_up_left_check(row, col, matrix):
    coordinates = list()
    while row in range(len(matrix) - 1) and col > 0:
        row -= 1
        col -= 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


def diagonals_up_right_check(row, col, matrix):
    coordinates = list()

    while row > 0 and col in range(len(matrix) - 1):
        row -= 1
        col += 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


def diagonals_down_left_check(row, col, matrix):
    coordinates = list()

    while row in range(len(matrix) - 1) and col > 0:
        row += 1
        col -= 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


def diagonals_down_right_check(row, col, matrix):
    coordinates = list()

    while row in range(len(matrix) - 1) and col in range(len(matrix) - 1):
        row += 1
        col += 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


def row_left_check(row, col, matrix):
    coordinates = list()
    while row > 0:
        row -= 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


def row_right_check(row, col, matrix):
    coordinates = list()

    while row in range(len(matrix) - 1):
        row += 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


def column_left_check(row, col, matrix):
    coordinates = list()

    while col > 0:
        col -= 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


def column_right_check(row, col, matrix):
    coordinates = list()

    while col in range(len(matrix) - 1):
        col += 1
        if matrix[row][col] == 'Q':
            coordinates.append([row, col])
            return coordinates


chess_boar_size = 8

chess_board = []

king_row = 0
king_col = 0

for i in range(chess_boar_size):
    new_row = input().split()
    for el in new_row:
        if el == 'K':
            king_row = i
            king_col = new_row.index(el)
            break
    chess_board.append(new_row)

queens = list()
counter = 0
queens.append(column_left_check(king_row, king_col, chess_board))
queens.append(row_left_check(king_row, king_col, chess_board))
queens.append(diagonals_down_left_check(king_row, king_col, chess_board))
queens.append(diagonals_up_left_check(king_row, king_col, chess_board))
queens.append(column_right_check(king_row, king_col, chess_board))
queens.append(row_right_check(king_row, king_col, chess_board))
queens.append(diagonals_down_right_check(king_row, king_col, chess_board))
queens.append(diagonals_up_right_check(king_row, king_col, chess_board))
for position in queens:
    if position:
        print(position[0])
        counter += 1

if counter == 0:
    print('The king is safe!')
