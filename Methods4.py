'''Create 5 objects initialize using parameterized constructor and access the object using instance
method and declare the mutator methods as set product name and set product price
and change the values of their properties using mutator methods and print it'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Mutator methods
    def set_product_name(self, name):
        self.name = name

    def set_product_price(self, price):
        self.price = price

    # Instance method to display product info
    def display(self):
        print(f"Product Name: {self.name}, Product Price: {self.price}")

# Create 5 objects
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
p3 = Product("Tablet", 15000)
p4 = Product("Monitor", 10000)
p5 = Product("Keyboard", 2000)

# Access and print using instance method
p1.display()
p2.display()
p3.display()
p4.display()
p5.display()

# Change values using mutator methods
p1.set_product_name("Gaming Laptop")
p1.set_product_price(70000)
p2.set_product_name("Smartphone")
p2.set_product_price(25000)

# Print updated values
print("\nAfter updating values:")
p1.display()
p2.display()