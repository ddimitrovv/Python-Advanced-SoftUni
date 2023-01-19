# Write a program that reads a text file,
# inserts line numbers in front of each line,
# and counts all the letters and punctuation marks.
# The result should be written to another text file.
from string import punctuation


def symbols_punctuation_counter(row):

    punctuations = set(punctuation)
    punctuation_marks = 0
    symbols = 0
    for ch in row:
        if ch.isalpha():
            symbols += 1
        if ch in punctuations:
            punctuation_marks += 1
    return symbols, punctuation_marks


with open('./text.txt', 'r') as file, open('./output.txt', 'w') as output_file:
    for idx, file_row in enumerate(file):
        letters, punctuation_symbols = symbols_punctuation_counter(file_row.strip())
        output_file.write(f'Line {idx + 1}: {file_row.strip()} ({letters})({punctuation_symbols})\n')
