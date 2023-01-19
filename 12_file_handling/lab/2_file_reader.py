# You are given a file called numbers.txt with the following content:
# 1
# 2
# 3
# 4
# 5
# Create a program that reads the numbers from the file.
# Print on the console the sum of those numbers.

sum_numbers = 0
file = open('./numbers.txt', 'r')
for number in file:
    sum_numbers += int(number)
print(sum_numbers)
