t = int(input("Enter number of test cases: "))
for _ in range(t):  
    values = input("Enter values (a b c x y): ").split() 
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    x = int(values[3])
    y = int(values[4]) 
    if a + b + c != x + y:
        print("NO")
    elif max(x, y) > max(a + b, b + c, c + a):
        print("NO")
    else:
        print("YES")
