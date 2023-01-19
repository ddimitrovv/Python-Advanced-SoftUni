# Write a program that reads a list of words from the file words.txt
# and finds how many times each of the words is contained in another file text.txt.
# Matching should be case-insensitive.
# The results should be written to other text files.
# Sort the words by frequency in descending order.
import re


def read_words():
    with open('./words.txt', 'r') as file:
        return file.read().split(' ')


def count_words_in_file(words):
    words_count = {
        word: 0 for word in words
    }
    with open('input.txt', 'r') as file:
        for line in file:
            words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
            for word in words:
                words_count[word] += words_in_line.count(word)

    return words_count


print(
    count_words_in_file(read_words())
)