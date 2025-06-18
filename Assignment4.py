'''Write a python program to create a SquareShape class & declare the properties as
Length
Breadth
Height
i)calculate the area of square using Instance methods.
ii)Check whether the Sides of Square's are equal or not using instance methods.
iii)calculate the perimeter of square using Instance methods.
iv)Find the Diagnols of Square using Instance methods.
v)Find the side length of square using instance method.'''
import math
class SquareShape:
    def __init__(self, length):
        self.length = length
        self.breadth = length
        self.height = length
    def calculate_area(self):
        return self.length * self.breadth
    def check_equal_sides(self):
        return self.length == self.breadth
    def calculate_perimeter(self):
        return 4 * self.length
    def find_diagonals(self):
        diagonal = math.sqrt(2) * self.length
        return diagonal
    def get_side_length(self):
        return self.length
if __name__ == "__main__":
    square = SquareShape(5)
    print("Area of the square:", square.calculate_area())
    print("Are all sides equal?", square.check_equal_sides())
    print("Perimeter of the square:", square.calculate_perimeter())
    print("Length of the diagonals:", square.find_diagonals())
    print("Side length of the square:", square.get_side_length())