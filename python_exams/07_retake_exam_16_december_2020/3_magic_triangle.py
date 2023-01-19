# Create a function called get_magic_triangle which will receive a single parameter (integer n)
# and it should create a magic triangle which follows those rules:
#     • We start with this simple triangle [[1], [1, 1]]
#     • We generate the next rows until we reach n amount of rows
#     • Each number in each row is equal to the sum of the two numbers right above it in the triangle
#     • If the current number has no neighbor to the upper left/right, we just take the existing neighbor
# After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5
#
# Note: Submit only the function in the judge system
# Input
#     • There will be no inputs
#     • The function will be tested by passing different values of n
#     • You can test your function with the test code below
# Constraints
#     • N will be in range [2, 100]

def get_magic_triangle(triangle_size):
    magic_triangle = []
    number = 1

    for row_index in range(1, triangle_size + 1):

        next_row = [0 for i in range(row_index)]
        for col_index in range(len(next_row)):
            if col_index == 0 or col_index == len(next_row) - 1:
                next_row[col_index] = number
            else:
                num = magic_triangle[-1][col_index] + magic_triangle[-1][col_index - 1]
                next_row[col_index] = num
        magic_triangle.append(next_row)

    return magic_triangle


print(get_magic_triangle(5))
