import numpy as np
import matplotlib.pyplot as plt
#Plot1:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(1,2,1)
plt.title("Plot-1")
plt.plot(x,y)
#Plot2:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.title("Plot-2")
plt.plot(x,y)
plt.show()
