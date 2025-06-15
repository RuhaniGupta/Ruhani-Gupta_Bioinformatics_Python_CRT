#write a python program to check whether the user given number is:
#prime number or not using functions(using return)
def prime_number(n,i=2):
    if(n<2):
        return False
    if(i*i>n):
        return True
    if(n%2==0):
        return False
    return prime_number(n,i+1) 
print(prime_number(10))
print(prime_number(11))

