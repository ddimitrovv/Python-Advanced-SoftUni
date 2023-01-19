# Write a function called fill_the_box that receives a different number of arguments representing:
#     • the height of a box
#     • the length of a box
#     • the width of a box
#     • n-times a different number of cubes with exact size 1 x 1 x 1
#     • a string "Finish"
# Your task is to fill the box with the given cubes until the current argument equals "Finish".
# Note: Submit only the function in the judge system
# Input
#     • There will be no input. Just parameters passed to your function.
# Output
# The function should return a string in the following format:
#     • If, at the end, there is free space left in the box, print:
#         ◦ "There is free space in the box. You could put {free space in cubes} more cubes."
#     • If there is no free space in the box, print:
#         ◦ "No more free space! You have {cubes left} more cubes."

def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    left_boxes = 0

    for item in args:
        if item == 'Finish':
            break

        boxes = int(item)
        if box_volume >= boxes:
            box_volume -= boxes
        else:
            boxes -= box_volume
            left_boxes += boxes
            box_volume = 0

    if left_boxes == 0:
        return f'There is free space in the box. You could put {box_volume} more cubes.'
    else:
        return f'No more free space! You have {left_boxes} more cubes.'


# ---- TEST CODE----

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
