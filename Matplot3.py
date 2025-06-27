#loc = left , right , center
#Grid for gridlines
import numpy as np
import matplotlib.pyplot as plt
x=np.array([10,34,64,78,56,8,76,54])
y=np.array([10,23,45,67,87,98,99,100])
plt.plot(x,y)
plt.title("Sports with Data", loc = 'center')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()