# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number
# in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.

numbers = [float(x) for x in input().split()]

occurrences = dict()

for number in numbers:
    if number not in occurrences:
        occurrences[number] = 0

    occurrences[number] += 1

for number, count in occurrences.items():
    print(f'{number:.1f} - {count} times')
