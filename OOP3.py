class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is Created")
        self.EmpName=empname
        self.EmpId=empID
        self.Designation=designation
        self.Salary=salary
        self.DeptName=deptname
def Display_Details(self):
    print("Details of Employees :")
    print(f"Employee Name : {self.EmpName}")
    print(f"Employee ID : {self.EmpId}")
    print(f"Employee's Designation : {self.Designation}")
    print(f"Employee's Salary : {self.Salary}")
    print(f"Employee DeptName : {self.DeptName}")
E1=Employee("Scott",'EMP101','Data Analyst',2500,'Deployment Team')
E2=Employee("Ram",'EMP102','Data Scientist',2600,'Bioinformatics')
E3=Employee("Preeti",'EMP104','Python Developer',2700,'BioTech')
E4=Employee("Sakshi",'EMP103','Python programmer',2300,'Biomedical')
E5=Employee("Sneha",'EMP107','Java developer',2800,'IT')
Display_Details(E1)
Display_Details(E2)
Display_Details(E3)
Display_Details(E4)
