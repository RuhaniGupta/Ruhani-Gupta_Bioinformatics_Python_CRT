#Locate Row
#Pandas use to loc attribute to return one or more specified row(s)
import pandas as pd
calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)
#Refer to the row index
print(myvar.iloc[0])
#Use of list of indexes
print(myvar.iloc[[0,1]])
#Locate named indexes
#Refer to the named index:
print(myvar.loc["day2"])