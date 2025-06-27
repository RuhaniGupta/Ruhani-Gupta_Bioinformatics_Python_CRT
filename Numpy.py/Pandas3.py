#Create Pandas Series from Dictionary
import pandas as pd
calories = {"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories)
print(myvar)

#Only specific items
import pandas as pd
calories = {"day1":420,"day2":380,"day3":390}
myvar = pd.Series(calories,items = ["day1","day2"])
print(myvar)