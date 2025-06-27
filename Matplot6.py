import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3])
y=np.array([4,9,1,10])
plt.title("Plot-1")
plt.subplot(2,3,1)
plt.plot(x,y)
#Plot2:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("Plot-2")
plt.subplot(2,3,2)
plt.plot(x,y)
#Plot3:
x=np.array([0,1,2,3])
y=np.array([4,9,1,10])
plt.title("Plot-3")
plt.subplot(2,3,3)
plt.plot(x,y)
#Plot4:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("Plot-4")
plt.subplot(2,3,4)
plt.plot(x,y)
#Plot5:
x=np.array([0,1,2,3])
y=np.array([4,9,1,10])
plt.title("Plot-5")
plt.subplot(2,3,5)
plt.plot(x,y)
#Plot6:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.title("Plot-6")
plt.subplot(2,3,6)
plt.plot(x,y)
plt.suptitle("MY SHOP")
plt.show()