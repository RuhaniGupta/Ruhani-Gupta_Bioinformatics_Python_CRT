class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        print("Object is Created")
        self.EmpName=empname
        self.EmpId=empID
        self.Designation=designation
        self.Salary=salary
        self.DeptName=deptname
    def Get_Details(self):
        print(self.EmpName)
        print(self.EmpId)
        print(self.Designation)
        print(self.Salary)
        print(self.DeptName)
E1=Employee("Scott",'EMP101','Data Analyst',2500,'Deployment Team')
E1.Get_Details()