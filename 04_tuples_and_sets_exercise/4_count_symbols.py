# Write a program that reads a text from the console and
# counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.

text = input()
chars = dict()

for ch in text:
    if ch not in chars:
        chars[ch] = 0
    chars[ch] += 1

for key, value in sorted(chars.items()):
    print(f"{key}: {value} time/s")
