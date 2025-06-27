import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print("Original Array :",arr)
print("Splitted Array :",newarr)
print("-----------------------")

#Splitting 2D array :
import numpy as np
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
newarr=np.array_split(arr,3)
print("Original Array :",arr)
print("Splitted Array :",newarr)
print("-----------------------")

#Searching array:where method is used
import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)

#Fixing indexes are even
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
x=np.where(arr%2==0)
print(x)

#Fixing indexes are odd
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
x=np.where(arr%2==1)
print(x)