# Write a function called multiply that can receive any quantity of numbers (integers)
# as different parameters and returns the result of the multiplication of all of them.
# Submit only your function in the Judge system.

def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
