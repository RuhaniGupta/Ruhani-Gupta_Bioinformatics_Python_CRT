'''You have attended a Skill Development Training Program for 15 Days on Python Programming Language
Write a python program to give the detailed report of 15 days python training which includes
1.Day
2.Topics Covered
3.Efficiency(rate of efficiency & grip on topics learnt on a scale of 5)
4.Number of Assignment Questions Solved
5.Number of Hackerank Questions Solved
6.Ratings Achieved on Hackerank for that particular day
7.Certifications Completed (including name of certificate)
8.Duration of Class
9.Rate of Class
i)1 -being worst
ii)2 -being hard
iii)3 -being averaqed
iv)4 - being '''

class python_report():
    def __init__(self,day,topics,efficiency,assignment,hackerank,ratings,certification,duration,rate):
        self.Day=day
        self.Topics=topics
        self.Efficiency=efficiency
        self.Assignment=assignment
        self.Hackerank=hackerank
        self.Ratings=ratings
        self.Certification=certification
        self.Duration=duration
        self.Rate=rate
def Display_Details(self):
    print(f"for the day is {self.Day}")
    print(f"the topics covered are {self.Topics}")
    print(f"efficiency{self.Efficiency}")
    print(f"the number of assignment questions{self.Assignment}")
    print(f"the number of hackerank questions{self.Hackerank}")
    print(f"Ratings Achieved on Hackerank for that particular day{self.Ratings}")
    print(f"Certifications Completed (including name of certificate){self.Certification}")
    print(f"Duration of Class{self.Duration}")
    print(f"Rate of Class{self.Rate}")
p1=python_report("Day1","Python variables","datatypes","high","15","4","None","12","8")
p2=python_report("Day2","Basics","CSS","high","15","4","None","1","7")
p3=python_report("Day3","C++","forloops","high","15","4","None","12","9")
p4=python_report("Day4","Java","loops","high","15","4","None","12","8")
p5=python_report("Day5","tuples","datatypes","Medium","15","4","None","12","5")
p6=python_report("Day6","integers","dataStructure","high","15","4","None","12","8")
p7=python_report("Day7","Python boolean","datatypes","Low","15","4","None","12","6")
p8=python_report("Day8","Strings","Arithmatic","high","15","4","None","2","8")
p9=python_report("Day9","Python OOPs","datatypes","high","15","4","None","2","7")
Display_Details(p1)
Display_Details(p2)
Display_Details(p3)
Display_Details(p4)
Display_Details(p5)
Display_Details(p6)
Display_Details(p7)
Display_Details(p8)
Display_Details(p9)
