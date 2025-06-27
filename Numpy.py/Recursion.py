'''Recusion Syntax in python
def function_name(parameters):
    if base_condition:
        return result
    return function_name(modified_parameters)
    '''
n=10
Sum=0
def Add_List(n,Sum):
        if bool(n):
            Sum=Sum+n
            return Sum
        return Add_List(n-1,Sum)
print(Add_List(5,0))

#Modified Parameter
def Add_List(n, Sum):
    if bool(n):
        return Sum+n
        return Add_List(n - 1, Sum )
    return Sum
print(Add_List(5,0))


