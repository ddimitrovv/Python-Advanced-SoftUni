# Write a function called operate that receives an operator ("+", "-", "*" or "/")
# as first argument and multiple numbers (integers) as additional arguments (*args).
# The function should return the result of the operator applied to all the numbers.
# For more clarification, see the examples below.
# Submit only your function in the Judge system.
# Note: Be careful when you have multiplication and division

def operate(operator, y, *args):
    def add():
        result = y
        for i in args:
            result += i
        return result

    def subtract():
        result = y
        for i in args:
            result -= i
        return result

    def divide():
        if y == 0:
            return
        result = y
        for i in args:
            result /= i
        return result

    def multiply():

        result = y
        for i in args:
            result *= i
        return result

    if operator == '+':
        return add()
    if operator == '-':
        return subtract()
    if operator == '/':
        return divide()
    if operator == '*':
        return multiply()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate('-', 1, 5, -7))
print(operate('/', 6, 8, 2))
