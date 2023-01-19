# Write a program that reads a number - N, representing the rows and columns of a square matrix.
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
# After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix
# and print its position in the format: "({row}, {col})". You should start searching from the top left.
# If there is no such symbol, print the message "{symbol} does not occur in the matrix".

n = int(input())

matrix = [input() for _ in range(n)]

symbol = input()

symbol_found = False

for row_index in range(n):
    if symbol in matrix[row_index]:
        symbol_found = True
        print(f"({row_index}, {matrix[row_index].index(symbol)})")
        break
else:
    print(f"{symbol} does not occur in the matrix")
