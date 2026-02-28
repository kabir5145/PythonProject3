import pandas as pd

# print(pd.__version__)

# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#          think of it like a single column in a spreadsheet  (1-Dimensional)

# data = [100,102,104,202,200]
# series = pd.Series(data , index = ["a","b","c","d","e"])
# print(series)

# series.loc["c"]= 200 #Locating a value by label
# print(series["c"])

# print(series.loc["a"])

# print(series.iloc[1]) #Locate by integer position

# print(series[series < 200])

calories = {"Day 1": 1750,
            "Day 2": 2100,
            "Day 3": 1700,}

series = pd.Series(calories)

# series.loc["Day 3"] += 500

# print(series.loc["Day 3"])


print(series[series < 2000])