# You will receive a sequence of numbers (integers) separated by a single space.
# Separate the negative numbers from the positive.
# Find the total sum of the negatives and positives, and print the following:
#     • On the first line, print the sum of the negatives
#     • On the second line, print the sum of the positives
#     • On the third line:
#         ◦ If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
#         ◦ If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"
# Note: you will not receive any zeroes in the input.

def negative_vs_positive(*args):
    negative = 0
    positive = 0
    for num in args:
        if num <= 0:
            negative += num
        else:
            positive += num

    return negative, positive


numbers_info = [int(x) for x in input().split()]

negative_nums, positive_nums = negative_vs_positive(*numbers_info)


print(negative_nums)
print(positive_nums)

if abs(negative_nums) > positive_nums:
    print('The negatives are stronger than the positives')

else:

    print('The positives are stronger than the negatives')
