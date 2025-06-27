'''Within the same class having multiple constructors with same name but 
different signature is called Constructor Overloading'''

'''
Write a python program to create an employee class and declare the states and create 5 objects 
different constructors.'''
class Employee:
    def __init__(self, name=None, emp_id=None, department=None, salary=None):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Dept: {self.department}, Salary: {self.salary}")

# Creating 5 objects using different constructor arguments
emp1 = Employee()  # No arguments
emp2 = Employee("Alice")  # Only name
emp3 = Employee("Bob", 102)  # Name and ID
emp4 = Employee("Charlie", 103, "HR")  # Name, ID, and Department
emp5 = Employee("David", 104, "IT", 50000)  # All arguments

emp1.display()
emp2.display()
emp3.display()
emp4.display()
emp5.display()


