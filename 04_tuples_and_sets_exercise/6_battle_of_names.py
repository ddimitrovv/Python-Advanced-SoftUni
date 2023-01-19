# You will receive a number N. On the following N lines, you will be receiving names.
# You should sum the ASCII values of each letter in the name and integer divide it to
# the number of the current row (starting from 1). Save the result to a set of either odd or even numbers,
# depending on if the resulting number is odd or even. After that, sum the values of each set.
#     • If the sums of the two sets are equal, print the union of the values, separated by ", ".
#     • If the sum of the odd numbers is bigger than the sum of the even numbers,
#       print the different values, separated by ", ".
#     • If the sum of the even numbers is bigger than the sum of the odd numbers,
#       print the symmetric-different values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set

n = int(input())

even_numbers = set()
odd_numbers = set()

for i in range(n):
    name = input()
    sum_chars = sum(ord(x) for x in name) // (i + 1)

    if sum_chars % 2 == 0:
        even_numbers.add(sum_chars)
    else:
        odd_numbers.add(sum_chars)

sum_even = sum(even_numbers)
sum_odd = sum(odd_numbers)

if sum_even == sum_odd:
    result = odd_numbers.union(even_numbers)
elif sum_odd < sum_even:
    result = odd_numbers.symmetric_difference(even_numbers)
else:
    result = odd_numbers.difference(even_numbers)

print(*result, sep=', ')
