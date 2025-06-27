'''Method Overloading:           |             
Within the same class having     |
multiple methods with same name  |
but different parameters is      |    
called Method Overloading.       |        '''

class Mobile:
    def __init__(self):
        print("Object is Created")
    def UnlockMobile(self):
        print("Swipe up to Unlock Your Mobile...!")
    UnlockMobile()
    def UnlockMobile(Password):
        print("Enter Password to Unlock Your Mobile...!")
    UnlockMobile("XYZ123")
    def UnlockMobile(Num,Pattern):
        print("Enter Your Pin to Unlock Your Mobile...!")
    UnlockMobile(4,"AAA")

