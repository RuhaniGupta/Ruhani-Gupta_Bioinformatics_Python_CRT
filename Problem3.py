'''
Sort and Remove Duplicates
Problem:
Given a list of integers that may contain duplicates, sort the list in ascending order and
remove all duplicates.

Input:

A list of integers arr with length n (1 ≤ n ≤ 1000)

Output:

Sorted list with unique elements only
--------------------------------------------
Input: [4, 2, 2, 8, 4, 6] 
Output: [2, 4, 6, 8]
'''
def sort_and_remove_duplicates(arr):
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    n = len(unique)
    for i in range(1, n):
        key = unique[i]
        j = i - 1
        while j >= 0 and unique[j] > key:
            unique[j + 1] = unique[j]
            j -= 1
        unique[j + 1] = key
    return unique
arr = [4, 2, 2, 8, 4, 6]
result = sort_and_remove_duplicates(arr)
print(result)