#Positional arguments
def pw(x,y):
    z=x**y
    print(z)
pw (5,2)

#keyword arguments
def show(name,age):
    print(name,age)
show(name="ruhi",age=62)

#default arguments
def show(name,age=27):
    print(name,age)
    show(name="sona",age=62)

#Variable Length Arguments
def Display(*x):
    x=x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]
    print(x)
Display(10,10,10,10,10,10,10)

#Keyword Variable length Arguments
def add(**num):
    z=num['a']+num['b']+num['c']
    print(z)
add(a=5,b=2,c=4)