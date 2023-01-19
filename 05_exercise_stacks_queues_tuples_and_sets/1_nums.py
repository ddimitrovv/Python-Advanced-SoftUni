# First, you will be given two sequences of integers values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
#     • "Add First {numbers, separated by a space}" - add the given numbers
#       at the end of the first sequence of numbers.
#     • "Add Second {numbers, separated by a space}" - add the given numbers
#       at the end of the second sequence of numbers.
#     • "Remove First {numbers, separated by a space}" - remove only the numbers
#       contained in the first sequence.
#     • "Remove Second {numbers, separated by a space}" - remove only the numbers
#       contained in the second sequence.
#     • "Check Subset" - check if any of the given sequences are a subset of the other.
#     If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ".
# The values in each sequence should be sorted in ascending order.

first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    info = input().split()
    first_second = info[1]
    add_remove = info[0]
    if add_remove == "Add":
        if first_second == "First":
            first = first.union([int(x) for x in info[2:]])
        else:
            second = second.union([int(x) for x in info[2:]])
    elif add_remove == "Remove":
        if first_second == "First":
            first = first.difference([int(x) for x in info[2:]])
        else:
            second = second.difference([int(x) for x in info[2:]])
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
