'''Comprehension contain very compact code usually a single statement that performs a task.
List Comprehension
Set Comprehension
Dictionary Comprehension
'''
'''
List Comprehension: List Comprehension represents creation of new list from an iterable object that satisfy 
given condition
Syntax:
new_list=[expression for new item in iterable_object_if_statement]
There can be zeroes or more if statement
There can be one or multiple for loops.

Ex:
list1=[i+1 for in in range(20)]
list2=[i for i in range(20)if i%2==0]
list3=[i for i in range(11)if i%2==0 if i%3==0]
'''