#copy
import numpy as np
arr=np.copy([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)
print(x)

#view
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=42
print(arr)
print(x)