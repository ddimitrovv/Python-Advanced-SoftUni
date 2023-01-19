# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8,
# and columns are marked from A to H. We have a total of 64 squares.
# Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
# In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
#     • Only move forward in a straight line:
#             ▪ White (w) moves from the 1st rank to the 8th rank direction.
#             ▪ Black (b) moves from 8th rank to the 1st rank direction.
#     • Can move only 1 square at a time.
#     • Can capture another pawn in from of them only diagonally:
#
# When a pawn reaches the last rank (for the white one - this is the 8th rank,
# and for the black one - this is the 1st rank), can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord.
# The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.
#
#
# Some rules apply when moving paws:
#     • If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
#     When a pawn captures another pawn, the game is over.
#     • If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
# Input
#     • On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
#         ◦ Empty positions are marked with "-".
#         ◦ White pawn is marked with "w"
#         ◦ Black pawn is marked with "b"
# Output
# Print either one of the following:
#     • If a pawn captures the other, print:
#         ◦ "Game over! {White/Black} win, capture on {square}."
#     • If a pawn reaches the last rank, print:
#         ◦ "Game over! {White/Black} pawn is promoted to a queen at {square}."
# Constraints
#     • The input will always be valid.
#     • The matrix will always be 8x8.
#     • There will be no case where two pawns are placed on the same square.
#     • There will be no case where two pawns are placed on the same column.
#     • There will be no case where black/white will be placed on the last rank.

def get_next_position_white(current_row, current_col, board):
    if current_col - 1 >= 0:
        if board[current_row - 1][current_col - 1] == 'b':
            return current_row - 1, current_col - 1, 'captured'
    if current_col + 1 < len(board):
        if board[current_row - 1][current_col + 1] == 'b':
            return current_row - 1, current_col + 1, 'captured'

    return current_row - 1, current_col, ''


def get_next_position_black(current_row, current_col, board):
    if current_col - 1 >= 0:
        if board[current_row + 1][current_col - 1] == 'w':
            return current_row + 1, current_col - 1, 'captured'
    if current_col + 1 < len(board):
        if board[current_row + 1][current_col + 1] == 'w':
            return current_row + 1, current_col + 1, 'captured'

    return current_row + 1, current_col, ''


chess_board_size = 8

chess_board = []

white_row, white_col = 0, 0
black_row, black_col = 0, 0

for i in range(chess_board_size):
    new_row = [x for x in input().split()]
    for j in range(len(new_row)):
        if new_row[j] == 'w':
            white_row, white_col = i, j
        if new_row[j] == 'b':
            black_row, black_col = i, j
    chess_board.append(new_row)

move_counter = 1
winner = ''
winner_row, winner_col = 0, 0
condition = ''
while True:
    next_row, next_col = 0, 0
    current_player = 'White' if move_counter % 2 != 0 else 'Black'

    if current_player == 'White':
        next_row, next_col, condition = get_next_position_white(white_row, white_col, chess_board)
        chess_board[white_row][white_col] = '-'
        chess_board[next_row][next_col] = 'w'
        white_row, white_col = next_row, next_col
        if white_row == 0:
            condition = 'promoted'

    if current_player == 'Black':
        next_row, next_col, condition = get_next_position_black(black_row, black_col, chess_board)
        chess_board[black_row][black_col] = '-'
        chess_board[next_row][next_col] = 'b'
        black_row, black_col = next_row, next_col
        if black_row == chess_board_size - 1:
            condition = 'promoted'

    if condition != '':
        winner_row, winner_col = next_row, next_col
        winner = current_player
        break
    move_counter += 1

winner_position = [[8, 7, 6, 5, 4, 3, 2, 1], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]

if condition == 'promoted':
    print(f"Game over! {winner} pawn is promoted to a queen at "
          f"{winner_position[1][winner_col]}{winner_position[0][winner_row]}.")
else:
    print(f"Game over! {winner} win, capture on "
          f"{winner_position[1][winner_col]}{winner_position[0][winner_row]}.")
