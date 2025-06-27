#Write a python program to print the summation of list element using recursion.
Li=[1,2,3,4,5]
def Add_List(List, Sum):
    if bool(List[len(List)-1]):
        Sum=Sum+List[len(List)-1]
        return Add_List(List.pop(),Sum)
    return Sum
print(Add_List(Li,0))

