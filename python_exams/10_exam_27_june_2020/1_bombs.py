# Ezio is still learning how to make bombs. With their help, he will save civilization.
# We should help Ezio to make his perfect bombs.
#
# You will be given two sequences of integers, representing bomb effects and bomb casings.
# You need to start from the first bomb effect and try to mix it with the last bomb casing.
# If the sum of their values is equal to any of the materials in the table below –
# create the bomb corresponding to the value and remove both bomb materials.
# Otherwise, just decrease the value of the bomb casing by 5.
# You need to stop combining when you have no more bomb effects or bomb casings,
# or you successfully filled the bombs pouch.
# Bombs:
#     • Datura Bombs: 40
#     • Cherry Bombs: 60
#     • Smoke Decoy Bombs: 120
# To fill the bomb pouch, Ezio needs three of each of the bomb types.
# Input
#     • On the first line, you will receive the integers representing the bomb effects, separated by ", ".
#     • On the second line, you will receive the integers representing the bomb casings, separated by ", ".
# Output
#     • On the first line, print:
#         ◦ if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"
#         ◦ if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."
#     • On the second line, print all bomb effects left:
#         ◦ If there are no bomb effects: "Bomb Effects: empty"
#         ◦ If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"
#     • On the third line, print all bomb casings left:
#         ◦ If there are no bomb casings: "Bomb Casings: empty"
#         ◦ If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"
#     • Then, you need to print all bombs and the count you have of them, ordered alphabetically:
#         ◦ "Cherry Bombs: {count}"
#         ◦ "Datura Bombs: {count}"
#         ◦ "Smoke Decoy Bombs: {count}"
# Constraints
#     • All the given numbers will be valid integers in the range [0, 120].
#     • There will be no cases with negative material.

from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = deque(int(x) for x in input().split(', '))

elements = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120,
}

values = [40, 60, 120]

elements_made = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

condition = False

while bomb_effects and bomb_casings:
    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    current_points = casing + effect
    if casing + effect in values:
        for name, points in elements.items():
            if current_points == points:
                if name not in elements_made:
                    elements_made[name] = 0
                elements_made[name] += 1
        counter = 0
        for value in elements_made.values():
            if value >= 3:
                counter += 1
                if counter == 3:
                    condition = True
        if condition:
            break
        continue
    bomb_effects.appendleft(effect)
    bomb_casings.append(casing - 5)


if condition:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')
else:
    print('Bomb Casings: empty')

for name, amount in sorted(elements_made.items()):
    print(f"{name}: {amount}")
