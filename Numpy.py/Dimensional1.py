'''Write a python program to create a one dimensional array with 15 elements and reshape into
 2 dimensional array with 3 rows and 5 columns.5rows and 3 columns and print the dimensions of it.
Reshape the same array into 3 dimensional array with 5 rows and 3 columns 1 element in each columns.'''
import numpy as np

# Step 1: Create a 1D array with 15 elements
arr = np.arange(1, 16)
print("Original 1D Array:")
print(arr)
print("Shape:", arr.shape)
print()

# Step 2: Reshape into 3 rows and 5 columns
arr_3x5 = arr.reshape(3, 5)
print("Reshaped to 2D (3 rows, 5 columns):")
print(arr_3x5)
print("Shape:", arr_3x5.shape)
print()

# Step 3: Reshape into 5 rows and 3 columns
arr_5x3 = arr.reshape(5, 3)
print("Reshaped to 2D (5 rows, 3 columns):")
print(arr_5x3)
print("Shape:", arr_5x3.shape)
print()

# Step 4: Reshape into 3D array (5 rows, 3 columns, 1 element each)
arr_3d = arr.reshape(5, 3, 1)
print("Reshaped to 3D (5 rows, 3 columns, 1 element each):")
print(arr_3d)
print("Shape:", arr_3d.shape)
