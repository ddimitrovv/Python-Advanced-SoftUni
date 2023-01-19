# Create a function called even_odd() that can receive a different quantity of numbers
# and a command at the end. The command can be "even" or "odd".
# Filter the numbers depending on the command and return them in a list.
# Submit only your function in the judge system.

def even_odd(*args):
    check = 0 if args[-1] == 'even' else 1
    nums = [x for x in args[:-1] if x % 2 == check]
    return nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
