# Write a program to flatten several lists of numbers received in the following format:
#     • String with numbers or empty strings separated by "|"
#     • Values are separated by spaces (" ", one or several)
#     • Order the output list from the last to the first matrix sub-lists
#       and their values from left to right


input_list = input().split("|")
final_list = list()
for index in range(len(input_list) - 1, -1, -1):
    current_elements = input_list[index].strip().split()
    final_list.extend(current_elements)

print(' '.join(final_list))
