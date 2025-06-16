#write a python program to chek whether the number is positive or negative using Lambda function
res=lambda n:print ("Positive") if (n>0) else (print("Zero") if(n==0) else print("Negative"))

#Another way to write the same program --------------------------------------------------------------------------------------------------
def Positive(Num):
    if(Num>0):
        print("+ve")
    else:
        if(Num==0):
            print("Zero")
        else:
            print("-ve")
Positive(0)