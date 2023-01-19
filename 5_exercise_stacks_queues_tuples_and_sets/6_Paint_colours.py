# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line
# containing substrings (separated by a single space) from which you will be able to form the following colors:
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check
# if you can get any of the above colors' names. If there is only one substring left,
# you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation
# could be formed from the given substrings:
#     • orange = red + yellow
#     • purple = red + blue
#     • green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
# When you form a color, remove both substrings. Otherwise, you should remove
# the last character of each substring and return them in the middle of the original string.
# If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring
# "re" and "bye", so you should remove the last character and return them in the middle of the string:
# "r by yellow".
# In the end, print out the list with colors in the order in which they are found.
# Input
#     • Single line string
# Output
#     • The list with the collected colors
# Constrains
#     • You will not receive an empty string
#     • Please consider only the colors mentioned above
#     • There won't be any cases with repeating colors

from collections import deque

info = deque([x for x in input().split()])

main_colours = (
    'red',
    'yellow',
    'blue'
)
secondary_colours = (
    'orange',
    'purple',
    'green'
)

collected_colours = list()
final_list = list()

forming_colours = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

while info:
    if len(info) == 1:
        first = info.popleft()
        second = ''
    else:
        first = info.popleft()
        second = info.pop()

    if first + second in main_colours:
        collected_colours.append(first + second)
        continue
    if second + first in main_colours:
        collected_colours.append(second + first)
        continue
    if first + second in secondary_colours:
        collected_colours.append(first + second)
        continue
    if second + first in secondary_colours:
        collected_colours.append(second + first)
        continue

    if len(first) > 1:
        info.insert((len(info) // 2), first[:-1])
    if len(second) > 1:
        info.insert((len(info) // 2), second[:-1])

for colour in collected_colours:
    if colour in main_colours:
        final_list.append(colour)
    if colour in secondary_colours:
        if forming_colours[colour][0] in collected_colours and forming_colours[colour][1] in collected_colours:
            final_list.append(colour)

print(final_list)
