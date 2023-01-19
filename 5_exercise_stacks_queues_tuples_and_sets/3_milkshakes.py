# First, you will be given two sequences of integers representing chocolates and cups of milk.
# You have to start from the last chocolate and try to match it with the first cup of milk.
# If their values are equal, you should make a milkshake and remove both ingredients.
# Otherwise, you should move the cup of milk at the end of the sequence and decrease the value
# of the chocolate by 5 without moving it from its position.
# If any of the values are equal to or below 0, you should remove them from the records
# right before mixing them with the other ingredient.
# When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate
# or cups of milk left, you need to stop making chocolate milkshakes.
# Input
#     • On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
#     • On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
# Output
#     • On the first line, print:
#         ◦ If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
#         ◦ Otherwise: "Not enough milkshakes."
#     • On the second line - print:
#         ◦ If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
#         ◦ Otherwise: "Chocolate: empty"
#     • On the third line - print:
#         ◦ If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
#         ◦ Otherwise: "Milk: empty"
# Constraints
#     • All given numbers will be valid integers in the range [-100 … 100].

from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milks = deque([int(x) for x in input().split(', ')])
milkshakes = 0

while chocolates and milks and milkshakes < 5:
    chocolate = chocolates.pop()
    milk = milks.popleft()

    if milk <= 0 and chocolate <= 0:
        continue
    if chocolate <= 0:
        milks.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        milks.appendleft(milk)


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join(str(x) for x in chocolates)}')
else:
    print('Chocolate: empty')
if milks:
    print(f'Milk: {", ".join(str(x) for x in milks)}')
else:
    print('Milk: empty')
