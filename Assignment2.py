'''Consider you are a HR Operations manager in Vignan Software Solutions,you are updating the Employee database,write a program to 
1. Add the Employee Details in your Company database which includes
Employee Name
Employee Id
Mail Id
Contact Number
Date of Joining
Background Verification (Just Mention YES or NO)
Probation Period(Just Mention YES or NO)
Notice Period(Just Mention YES or No)
Designation
Salary
2.Remove an employee from the Company db based on EMPLOYEE ID
3.Check the background verification(Just Mention YES or NO & print whether it is done or not) for an employee
4.Print the Final List/Dictionary of the Employee
5.Exit'''
class Employee:
    def __init__(self, name, emp_id, mail, contact, doj, bg_ver, probation, notice, designation, salary):
        self.name = name
        self.emp_id = emp_id
        self.mail = mail
        self.contact = contact
        self.doj = doj
        self.bg_ver = bg_ver
        self.probation = probation
        self.notice = notice
        self.designation = designation
        self.salary = salary

    def __str__(self):
        return (f"Name: {self.name}, ID: {self.emp_id}, Mail: {self.mail}, Contact: {self.contact}, "
                f"DOJ: {self.doj}, BG Verification: {self.bg_ver}, Probation: {self.probation}, "
                f"Notice: {self.notice}, Designation: {self.designation}, Salary: {self.salary}")

class EmployeeDB:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp):
        self.employees[emp.emp_id] = emp

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee with ID {emp_id} removed.")
        else:
            print("Employee ID not found.")

    def check_bg_verification(self, emp_id):
        emp = self.employees.get(emp_id)
        if emp:
            if emp.bg_ver.upper() == "YES":
                print(f"Background verification for {emp.name} is DONE.")
            else:
                print(f"Background verification for {emp.name} is NOT DONE.")
        else:
            print("Employee ID not found.")

    def print_all(self):
        if not self.employees:
            print("No employees in the database.")
        else:
            for emp in self.employees.values():
                print(emp)

db = EmployeeDB()
while True:
    print("\n1. Add Employee\n2. Remove Employee\n3. Check Background Verification\n4. Print All Employees\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Employee Name: ")
        emp_id = input("Employee ID: ")
        mail = input("Mail ID: ")
        contact = input("Contact Number: ")
        doj = input("Date of Joining: ")
        bg_ver = input("Background Verification (YES/NO): ")
        probation = input("Probation Period (YES/NO): ")
        notice = input("Notice Period (YES/NO): ")
        designation = input("Designation: ")
        salary = input("Salary: ")
        emp = Employee(name, emp_id, mail, contact, doj, bg_ver, probation, notice, designation, salary)
        db.add_employee(emp)
        print("Employee added successfully.")
    elif choice == "2":
        emp_id = input("Enter Employee ID to remove: ")
        db.remove_employee(emp_id)
    elif choice == "3":
        emp_id = input("Enter Employee ID to check BG verification: ")
        db.check_bg_verification(emp_id)
    elif choice == "4":
        db.print_all()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")