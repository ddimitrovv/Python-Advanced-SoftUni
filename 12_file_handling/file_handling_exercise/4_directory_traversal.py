# Write a program that traverses a given directory for all files.
# Search through the first level of the directory only
# and write information about each found file in report.txt.
# The files should be grouped by their extension.
# Extensions should be ordered by name alphabetically.
# The files with extensions should also be sorted by name.
# report.txt should be saved in the chosen directory.

from os import listdir
from os.path import isdir, join


def directory_search(path, files):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_search(join(path, element), files)
        else:
            extension = element.split('.')[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)


output = {}
input_path = input()
directory_search(input_path, output)

with open('./report.txt', 'w') as file:

    for key, value in sorted(output.items()):
        file.write(f'.{key}\n')
        for elem in sorted(value):
            file.write(f'- - - {elem}\n')
