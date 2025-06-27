'''A hospital stores stores the temperature readings of a patient for 7 days:
temps=np.array([98.4,98.6,99.1,100.2,98.9,99.5,98.7])
Using numpy find the maximum and minimum temperature recorded'''
import numpy as np
temps=np.array([98.4,98.6,99.1,100.2,98.9,99.5,98.7])
max_temp = np.max(temps)
min_temp = np.min(temps)
print("Maximum temperature:", max_temp)
print("Minimum temperature:", min_temp)

'''A teacher stores students scores in a NumPy array:
scores = np.array([45,67,89,76,55]) 
using NumPy,how many students scored more than 60'''
import numpy as np
scores = np.array([45, 67, 89, 76, 55])
count = np.sum(scores > 60)
print(count)

'''A retail shop stores item prices and quantities purchased:
prices=np.array([50,20,30])
quantities=np.array'''


'''A company collects feedback ratings from 10 user
ratings=np.array([4,3,5,4,2,5,3,4,5,1])
Using numpy.count how many users gave a rating of 5'''
import numpy as np
ratings = np.array([4, 3, 5, 4, 2, 5, 3, 4, 5, 1])
count = np.count_nonzero(ratings == 5)
print(count)

'''You have houses price (in lakhs) of a locality
houses_prices=np.array([45,50,48,52,47])
Increase each price by 10 percent using Numpy and display the updated prices'''
import numpy as np
houses_prices = np.array([45, 50, 48, 52, 47])
updated_prices = houses_prices * 1.10 
print(updated_prices)

'''A football player's goals in 5 matches
goals=np.array([1,0,2,1,3])
Find the average number of goals per match using Numpy'''
import numpy as np
goals = np.array([1, 0, 2, 1, 3])
average_goals = np.mean(goals)
print(average_goals)

'''A car tracks its mileage over 6 months(in km per liter)
mileage=np.array([15.2,16.5,14.8,15.9,16.2,15.5])
Using NumPy,find the months where mileage was less than 15.'''
import numpy as np
mileage = np.array([15.2, 16.5, 14.8, 15.9, 16.2, 15.5])
months_below_15 = np.where(mileage < 15)[0] + 1 
print("Mileage was less than 15 in month(s):", months_below_15)