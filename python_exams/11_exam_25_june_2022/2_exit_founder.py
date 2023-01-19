player_1, player_2 = input().split(', ')

matrix = [[x for x in input().split()] for _ in range(6)]

counter = 0

player_to_rest = []

while True:

    row, col = [int(x) for x in input() if x.isdigit()]
    player = player_1 if counter % 2 == 0 else player_2

    if player_to_rest and player_to_rest[0] == player:
        del player_to_rest[0]

    elif matrix[row][col] == 'E':
        print(f'{player} found the Exit and wins the game!')
        break
    elif matrix[row][col] == 'T':
        winner = player_1 if player == player_2 else player_2
        print(f'{player} is out of the game! The winner is {winner}.')
        break
    elif matrix[row][col] == 'W':
        print(f'{player} hits a wall and needs to rest.')
        player_to_rest.append(player)

    counter += 1
