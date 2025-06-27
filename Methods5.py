'''Write a python program to create a student class and declare the properties as Student name,
Student id, Branch,percentage,Age,Year of passout,Number of certifications has student have and 
create 10 objects and initialize the value using mutator method and access the value using 
accessor methods 
Note:(you have to initialize the value without using Constructor)'''
'''
write a py prog to create a student class and declare the properties (states) as 
student name, student_Id, branch, percentage, age, year of passing, number of certifications student had 
and create 10 objects and initialize the values using mutater method and access the values using accesor method
note: initialize the values without using constructor
'''
class Student():
    def Set_name(self):
        name = input("enter the name of the student: ")
        self.Name = name
    def Set_student_ID(self):
        sd_ID = input("enter the student ID: ")
        self.Sd_ID = sd_ID
    def Set_student_branch(self):
        branch = input("enter student branch: ")
        self.Branch = branch
    def Set_student_percentage(self):
        percentage = input("enter students percentage: ")
        self.Percentage = percentage
    def Set_student_age(self):
        age = input("enter students age: ")
        self.Age = age 
    def Set_student_year(self):
        year = input("enter student year of passing: ")
        self.Year = year
    def Set_student_certifications(self):
        certification = input("enter number of certifications students had: ")
        self.Certifications = certification
    def Get_name(self):
        print(f"Student name is: {self.Name}")
    def Get_student_ID(self):
        print(f"Student ID is: {self.Sd_ID}")
    def Get_student_branch(self):
        print(f"Branch of the student is: {self.Branch}")
    def Get_student_percentage(self):
        print(f"Percentage of the student is: {self.Percentage}")
    def Get_student_age(self):
        print(f"age of the student is {self.Age}")
    def Get_student_year(self):
        print(f"Student will be passed in the year of {self.Year}")
    def Get_student_certifications(self):
        print(f"There are {self.Certifications} for the student")
        S1 = Student()
        S1.Set_name()
        S1.Set_student_ID()
        S1.Set_student_branch()
        S1.Set_student_percentage()
        S1.Set_student_age()
        S1.Set_student_year()
        S1.Set_student_certifications()
        print("")
        S1.Get_name()
        S1.Get_student_ID()
        S1.Get_student_branch()
        S1.Get_student_percentage()
        S1.Get_student_age()
        S1.Get_student_year()
        S1.Get_student_certifications()


        S2 = Student()
        S2.Set_name()
        S2.Set_student_ID()
        S2.Set_student_branch()
        S2.Set_student_percentage()
        S2.Set_student_age()
        S2.Set_student_year()
        S2.Set_student_certifications()
        print("")

        S2.Get_name()
        S2.Get_student_ID()
        S2.Get_student_branch()
        S2.Get_student_percentage()
        S2.Get_student_age()
        S2.Get_student_year()
        S2.Get_student_certifications()

        S3 = Student()
        S3.Set_name()
        S3.Set_student_ID()
        S3.Set_student_branch()
        S3.Set_student_percentage()
        S3.Set_student_age()
        S3.Set_student_year()
        S3.Set_student_certifications()
        print("")

        S3.Get_name()
        S3.Get_student_ID()
        S3.Get_student_branch()
        S3.Get_student_percentage()
        S3.Get_student_age()
        S3.Get_student_year()
        S3.Get_student_certifications()

        S4 = Student()
        S4.Set_name()
        S4.Set_student_ID()
        S4.Set_student_branch()
        S4.Set_student_percentage()
        S4.Set_student_age()
        S4.Set_student_year()
        S4.Set_student_certifications()
        print("")

        S4.Get_name()
        S4.Get_student_ID()
        S4.Get_student_branch()
        S4.Get_student_percentage()
        S4.Get_student_age()
        S4.Get_student_year()
        S4.Get_student_certifications()

        S5 = Student()
        S5.Set_name()
        S5.Set_student_ID()
        S5.Set_student_branch()
        S5.Set_student_percentage()
        S5.Set_student_age()
        S5.Set_student_year()
        S5.Set_student_certifications()
        print("")

        S5.Get_name()
        S5.Get_student_ID()
        S5.Get_student_branch()
        S5.Get_student_percentage()
        S5.Get_student_age()
        S5.Get_student_year()
        S5.Get_student_certifications()

        S6 = Student()
        S6.Set_name()
        S6.Set_student_ID()
        S6.Set_student_branch()
        S6.Set_student_percentage()
        S6.Set_student_age()
        S6.Set_student_year()
        S6.Set_student_certifications()
        print("")