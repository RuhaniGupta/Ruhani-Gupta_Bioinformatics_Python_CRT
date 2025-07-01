'''write a python program to read the length of the string as input from the user and print all binary strings of length n.'''
#Generate all Binary Strings of length n
def generate_binary_no_backtracking(n):
    result = '0' * n
    print(result) 
generate_binary_no_backtracking(3)
#With backtracking
print("With Backtracking")
def generate_binary_backtrack(n, current=""):
    if len(current) == n:
        print(current)
        return
#Choose '0'
    generate_binary_backtrack(n, current + '0')
    #Choose '1'
    generate_binary_backtrack(n, current + '1')
generate_binary_backtrack(3)