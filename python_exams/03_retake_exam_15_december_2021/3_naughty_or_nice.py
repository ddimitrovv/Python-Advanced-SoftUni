# Santa Claus is always watching and seeing if children are good or bad.
# Only the nice children get Christmas presents,
# so Santa Claus is preparing his list this year to check which child has been good or bad.
# Write a function called naughty_or_nice_list which will receive
#     • A list representing Santa Claus' "Naughty or Nice" list full of kids' names
#     • A different number of arguments (strings) and/or keywords representing commands
# The function should sort the kids in the given Santa Claus list into 3 lists:
#   "Nice", "Naughty", and "Not found".
# The list holds a different number of kids - tuples containing two elements:
#   a counting number (integer) at the first position and a name (string) at the second position.
# For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
# Next, the function could receive arguments and/or keywords.
# Each argument is a command. The commands could be the following:
#     • "{counting_number}-Naughty" - if there is only one tuple in the given list with the same number,
#       MOVE the kid to a list with NAUGHTY kids and remove it from the Santa list.
#       Otherwise, ignore the command.
#     • "{counting_number}-Nice" - if there is only one tuple in the given list with the same number,
#       MOVE the kid to a list with NICE kids and remove it from the Santa list.
#       Otherwise, ignore the command.
# Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
#     • If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY
#       or to the list with NICE kids depending on the value in the keyword.
#       Then, remove it from the Santa list.
#     • Otherwise, ignore the command.
# All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
# In the end, return the final lists, each on a new line as described below.
# Note: Submit only the function in the judge system
# Input
#     • There will be no input. Just parameters passed to your function.
# Output
#     • The function should return strings with the names on each list on separate lines,
#     if there are any, otherwise skip the line:
#         ◦ "Nice: {name1}, {name2} … {nameN}"
#         ◦ "Naughty: {name1}, {name2} … {nameN}"
#         ◦ "Not found: {name1}, {name2} … {nameN}"

def repeating_or_missing_nums(list_santa, number):
    counter = 0
    for kid in list_santa:
        if kid[0] == number:
            counter += 1
    return True if counter != 1 else False


def repeating_or_missing_names(list_santa, name):
    counter = 0
    for kid in list_santa:
        if kid[1] == name:
            counter += 1
    return True if counter != 1 else False


def naughty_or_nice_list(santa_list, *args, **kwargs):
    naughty_kids = list()
    nice_kids = list()
    not_found = list()

    for kid_info in args:
        kid_info = kid_info.split('-')
        condition = kid_info[1]
        kid_num = int(kid_info[0])
        if repeating_or_missing_nums(santa_list, kid_num):
            continue
        for santa_kid_info in santa_list:
            if santa_kid_info[0] == kid_num:
                if condition == 'Nice':
                    nice_kids.append(santa_kid_info[1])
                if santa_kid_info[0] == kid_num:
                    if condition == 'Naughty':
                        naughty_kids.append(santa_kid_info[1])
                santa_list.remove(santa_kid_info)

    for name, condition in kwargs.items():
        if repeating_or_missing_names(santa_list, name):
            continue
        for santa_kid_info in santa_list:
            if santa_kid_info[1] == name:
                if condition == 'Nice':
                    nice_kids.append(name)
                if santa_kid_info[1] == name:
                    if condition == 'Naughty':
                        naughty_kids.append(name)
                santa_list.remove(santa_kid_info)

    while santa_list:
        kid = santa_list[0][1]
        not_found.append(kid)
        del santa_list[0]

    output = list()
    if nice_kids:
        output.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        output.append(f"Naughty: {', '.join(naughty_kids)}")
    if not_found:
        output.append(f"Not found: {', '.join(not_found)}")

    return '\n'.join(output)


print(naughty_or_nice_list(
        [
            (3, "Amy"),
            (1, "Tom"),
            (7, "George"),
            (3, "Katy"),
        ],
        "3-Nice",
        "1-Naughty",
        Amy="Nice",
        Katy="Naughty",
    )
)
print('-' * 30)
print(naughty_or_nice_list(
        [
            (7, "Peter"),
            (1, "Lilly"),
            (2, "Peter"),
            (12, "Peter"),
            (3, "Simon"),
        ],
        "3-Nice",
        "5-Naughty",
        "2-Nice",
        "1-Nice",
    )
)
print('-' * 30)
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
    )
)
