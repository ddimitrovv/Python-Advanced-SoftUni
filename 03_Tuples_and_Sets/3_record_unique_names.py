# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

n = int(input())

names = {input() for _ in range(n)}
[print(name) for name in names]
