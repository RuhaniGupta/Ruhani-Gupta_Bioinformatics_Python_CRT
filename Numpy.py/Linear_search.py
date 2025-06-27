def LinearSearch(key,arr,len):
    count = 0
    for i in range(len):
        count += i
        print(f"{count}Iteration")
        if arr[i]==key:
            print("Element not Found")
            break
    else:
        print("Element Found at {res} index")
res=LinearSearch(9,[5,6,7,4,2,1,0,8,9],10)