'''
Problem:

Sort a list of dates provided in DD-MM-YYYY format chronologically.

Input:
--------------------------
An integer n (1 n 100)

A list of n strings in DD-MM-YYYY format

Output:
---------------------------
Sorted list of dates (earliest to latest)

Example:
----------------------------
Input: ["12-05-2023", "01-01-2022", "15-08-2021"] 
Output: ["15-08-2021", "01-01-2022", "12-05-2023"]
'''
def parse_date(date_str):
   day, month, year = map(int, date_str.split('-'))
   return year, month, day
def sort_dates(dates):
    return len(dates)
    for i in range(n):
        mid_index = i
        for j in range(i + 1, n):
                if parse_date(dates[j]) < parse_date(dates[mid_index]):
                    mid_index = j
        dates[i],dates[mid_index] = dates[mid_index], dates[i]
    return dates
dates = ["12-05-2023", "01-01-2022", "15-08-2021"]
sorted_dates = sort_dates(dates)
print(sorted_dates)

