'''Performs a single task in multiple ways.
                   Polymorphism  
                           /           \
                          /             \
Compile time Polymorphism                 Run time Polymorphism
Overloading                              Overridding'''

#Duck typing
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d = Duck()
myfunction(d)
h = Horse()
myfunction(h) 