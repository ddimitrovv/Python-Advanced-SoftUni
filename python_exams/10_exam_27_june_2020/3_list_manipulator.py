# Write a function called list_manipulator which receives a list of numbers as first parameter
# and different amount of other parameters. The second parameter might be "add" or "remove".
# The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
#     • In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers
#       and return the new list
#     • In case of "add" and "end", add the given numbers to the end of the given list of numbers
#       and return the new list
#     • In case of "remove" and "beginning"
#         ◦ If there is another parameter (number), remove that amount of numbers from the beginning
#           of the list of numbers.
#         ◦ If there are no other parameters, remove only the first element of the list.
#         ◦ Finally, return the new list
#     • In case of "remove" and "end"
#         ◦ If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
#         ◦ Otherwise if there are no other parameters, remove only the last element of the list.
#         ◦ Finally, return the new list
# For more clarifications, see the examples below.
# Input
#     • There will be no input
#     • Parameters will be passed to your function
# Output
#     • The function should return the new list of numbers
def len_elements(my_list):
    return len(my_list) > 2


def add_to_list(my_list, pos, elements):

    numbers = [x for x in elements[2:]]

    if pos == 'beginning':
        for i in range(len(numbers) - 1, -1, -1):
            my_list.insert(0, numbers[i])
    if pos == 'end':
        for i in range(len(numbers)):
            my_list.append(numbers[i])
    return my_list


def remove_from_list(my_list, pos, elements):
    numbers = [x for x in elements[2:]]
    if not numbers:
        remove_range = 1
    else:
        remove_range = len(numbers) + 1

    if pos == 'beginning':
        for _ in range(remove_range):
            my_list.pop(0)
    if pos == 'end':
        for _ in range(remove_range):
            my_list.pop()

    return my_list


def list_manipulator(start_list, *args):
    command = args[0]
    position = args[1]

    if command == 'add':
        start_list = add_to_list(start_list, position, args)
    if command == 'remove':
        start_list = remove_from_list(start_list, position, args)

    return start_list


print(list_manipulator(
    [1, 2, 3],
    "remove",
    "end")
)
print(list_manipulator(
    [1, 2, 3],
    "remove",
    "beginning")
)
print(list_manipulator(
    [1, 2, 3],
    "add",
    "beginning",
    20)
)
print(list_manipulator(
    [1, 2, 3],
    "add",
    "end",
    30)
)
print(list_manipulator(
    [1, 2, 3],
    "remove",
    "end",
    2)
)
print(list_manipulator(
    [1, 2, 3],
    "remove",
    "beginning",
    2)
)
print(list_manipulator(
    [1, 2, 3],
    "add",
    "beginning",
    20,
    30,
    40)
)
print(list_manipulator(
    [1, 2, 3],
    "add",
    "end",
    30,
    40,
    50)
)