# Write a recursive function called palindrome() that will receive a word and an index (always 0).
# Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome
# and "{word} is not a palindrome" if the word is not a palindrome using recursion.
# Submit only the function in the judge system.

def palindrome(word, index):
    if index >= len(word) // 2:
        return f'{word} is a palindrome'
    left_letter = word[index]
    right_letter = word[-1 - index]
    if left_letter != right_letter:
        return f'{word} is not a palindrome'
    return palindrome(word, index + 1)


# ---- TEST CODE----

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
