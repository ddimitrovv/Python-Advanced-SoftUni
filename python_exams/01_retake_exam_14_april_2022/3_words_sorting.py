# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received.
# For each key, create a value that is the sum of all ASCII values of that key.
# Then, sort the dictionary:
#     • By values in descending order, if the sum of all values of the dictionary is odd
#     • By keys in ascending order, if the sum of all values of the dictionary is even
# Note: Submit only the function in the judge system
# Input
#     • There will be no input, just any number of words passed to your function
# Output
#     • The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
# Constraints:
#     • There will be no case with capital letters.
#     • There will be no case with a string consisting of other than letters.


def words_sorting(*args):
    ascii_dict = dict()

    for word in args:
        value = sum([ord(x) for x in word])
        if word not in ascii_dict.keys():
            ascii_dict[word] = value

    output = list()
    result = sum([value for key, value in ascii_dict.items()])
    if result % 2 != 0:
        for key, value in sorted(ascii_dict.items(), key=lambda x: x[1], reverse=True):
            output.append(f'{key} - {value}')
    if result % 2 == 0:
        for key, value in sorted(ascii_dict.items(), key=lambda x: x[0]):
            output.append(f'{key} - {value}')

    return '\n'.join(output)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    )
)

print('-' * 30)
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    )
)

print('-' * 30)
print(
    words_sorting(
        'cacophony',
        'accolade'
    )
)
