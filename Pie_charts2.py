#Labels:
import matplotlib.pyplot as plt
import numpy as np
y=np.array([10,10,15,20,12,13,20])
mylabels=["Python","C++","Java","C","SQL","Pandas","Numpy"] 
myexplode=[0,0.2,0.1,0,0.1,0,0.2]
plt.pie(y,labels=mylabels,startangle=360,explode=myexplode)
plt.legend(title="Programming Languages")
plt.show()