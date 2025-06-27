'''write a python program to create a rectangle class and initilize a variables length
 and breadth using constructor and access the values using mutator methods.'''
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Mutator methods
    def set_length(self, length):
        self.length = length

    def set_breadth(self, breadth):
        self.breadth = breadth

    # Method to display values
    def display(self):
        print(f"Length: {self.length}, Breadth: {self.breadth}")

# Example usage
rect = Rectangle(10, 5)
rect.display()

# Change values using mutator methods
rect.set_length(15)
rect.set_breadth(8)
rect.display()