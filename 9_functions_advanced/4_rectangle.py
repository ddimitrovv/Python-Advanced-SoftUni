# Create a function called rectangle(). It must have two parameters - length and width.
# First, you need to check if the given arguments are integers:
#     • If one/ both of them is/ are NOT an integer/s, return the string "Enter valid values!"
# Create two inner functions:
#     • area() - returns the area of the rectangle with the given length and width
#     • perimeter() - returns the perimeter of the rectangle with the given length and width
# In the end, the rectangle function should return a string containing the area
# and the perimeter of a rectangle in the following format:
# "Rectangle area: {rect_area}
# Rectangle perimeter: {rect_perim}"

def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values!'
    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print('----- Test 1 -----')

print(rectangle(2, 10))

print('----- Test 2 -----')

print(rectangle('2', 10))

#judge test
import unittest

class RectangleTests(unittest.TestCase):
   def test(self):
      result = rectangle(2, 10)
      self.assertEqual(result, "Rectangle area: 20\nRectangle perimeter: 24")
