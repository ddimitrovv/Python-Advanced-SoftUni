# Chess is the oldest game, but it is still popular these days.
# It will be used only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make, as illustrated.
# It can move to the nearest square but not on the same row, column,
# or diagonal. (e.g., it can move two squares horizontally, then one square vertically,
# or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells.
# Your task is to remove knights until no knights that can attack one another with one move are left.
# Input
#     • On the first line, you will receive integer N - the size of the board
#     • On the following N lines, you will receive strings with "K" and "0"
# Output
#     • Print a single integer with the minimum number of knights that need to be removed
# Constraints
#     • The size of the board will be 0 < N < 30
#     • Time limit: 0.3 sec. Memory limit: 16 MB

def check_max(matrix, row, col):
    knight_moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
    ]
    max_attack = 0
    for r, c in knight_moves:
        if r in range(len(matrix)) and c in range(len(matrix)) and matrix[r][c] == 'K':
            max_attack += 1
    return max_attack


board_size = int(input())

chess_board = []

for _ in range(board_size):
    chess_board.append([x for x in input()])

removed_knights = 0

while True:
    max_attacks = 0
    knight_row = 0
    knight_col = 0

    for row in range(board_size):
        for col in range(board_size):
            if chess_board[row][col] == '0':
                continue
            current_attack = check_max(chess_board, row, col)
            if current_attack > max_attacks:
                max_attacks = current_attack
                knight_row = row
                knight_col = col
    if max_attacks == 0:
        break

    chess_board[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
