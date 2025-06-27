'''1st loop 
2nd line decides number of chars for each line.
          
      *
    * *
  * * * 
* * * * '''



n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(0,i):
            print("* ",end="")
    print()



