#Labels:
import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,75,25,15])
mylabels=["Apple","Mango","Litchi","Grapes"] 
myexplode=[0,0,0.1,0]
plt.pie(y,labels=mylabels,startangle=360,explode=myexplode)
plt.legend(title="Four Fruits")
plt.show()