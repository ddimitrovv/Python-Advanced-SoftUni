# Create a program that will receive commands until the command "End".
# The commands can be:
#     • "Create-{file_name}" - Creates the given file with an empty content.
#       If the file already exists, remove the existing text in it (as if the file is created again)
#     • "Add-{file_name}-{content}" - Append the content and a new line after it.
#       If the file does not exist, create it, and add the content
#     • "Replace-{file_name}-{old_string}-{new_string}" -
#       Open the file and replace all the occurrences of the old string with the new string.
#       If the file does not exist, print: "An error occurred"
#     • "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"

from os import remove
from os.path import exists


def create_file(name):
    open(f'./{name}', 'w')


def add_to_file(name, content):
    with open(f'./{name}', 'a') as file:
        file.write(content + '\n')


def replace_strings_in_file(name, old, new):
    if not exists(f'./{name}'):
        print('An error occurred')
        return
    with open(f'./{name}', 'r+') as file:
        content = file.read().replace(old, new)
        file.seek(0)
        file.truncate()
        file.write(content)


def delete_file(name):
    if not exists(f'./{name}'):
        print('An error occurred')
        return
    remove(f'./{name}')


while True:
    info = input()
    if info == 'End':
        break
    info = info.split('-')
    command = info[0]
    file_name = info[1]

    if command == 'Create':
        create_file(file_name)

    if command == 'Add':
        new_content = info[2]
        add_to_file(file_name, new_content)

    if command == 'Replace':
        old_string, new_string = info[2], info[3]
        replace_strings_in_file(file_name, old_string, new_string)

    if command == 'Delete':
        delete_file(file_name)
