'''Write a python program to create a matrix with 4 rows and 4 columns using numpy library and 
give only multiples of 5'''
import numpy as np

# Create an array of multiples of 5 from 5 to 80 (16 elements)
arr = np.arange(5, 5*16+1, 5)
matrix = arr.reshape(4, 4)
print(matrix)