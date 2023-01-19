# Write a program that reads a text file and prints on the console it's even lines.
# Line numbers start from 0. Before you print the result,
# replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

symbols_to_replace = {"-", ",", ".", "!", "?"}
with open('./text.txt', 'r') as file:
    for idx, row in enumerate(file):
        if idx % 2 == 0:
            output = ' '.join(row.strip().split()[::-1])
            for char in symbols_to_replace:
                output = output.replace(char, '@')
            print(output)
