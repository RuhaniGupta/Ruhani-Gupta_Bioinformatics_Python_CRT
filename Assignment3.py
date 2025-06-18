'''Write a python program to a book calss declare states as
-->Book name
-->Auther name
-->publisher name
-->published date
-->category of book

i)Create 5 objects and initilize the values using constructor where 
out of five
-->Create 1 object using one paremetrized constructor
-->Create a 2nd object using 2 parameterized constructor
-->Create a 3rd object using zero parameterized constructor
-->Create a 4th object using four parameterized constructor
-->Create a 5th object using five parameterized constructor
ii)Acess the values using acessor methods
iii)update the values usingmutatot method for name of the book'''
class Book():
    def __init__(self,bookname=None,authername=None,publishername=None,publishdate=None,catogery=None):
        self.BookName=bookname
        self.AuthorName=authername
        self.Publisher=publishername
        self.Date=publishdate
        self.Catogery=catogery
    def get_details(self):
        print(f"The book name is:{self.BookName}")  
        print(f"Name of the author is:{self.AuthorName}")  
        print(f"Name of the publisher is:{self.Publisher}")
        print(f"Date of publication is:{self.Publisher}")
        print(f"Category is:{self.Catogery}")
        print("-----------------------------------")
    def set_bookName(self,new_name):
        self.name=new_name
book1=Book("python programming")
book2=Book('python programming','Ruhi')
book3=Book('')
book4=Book('oop','jam',123,345)
book5=Book('ads','hide',123,456,"team")
book1.get_details()
book2.get_details()
book3.get_details() 
book4.get_details()
print("after updating...")
book2.set_bookName('datastructures')
book2.get_details()




