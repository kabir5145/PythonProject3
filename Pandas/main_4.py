import pandas as pd

# .to_string() = To print whole data

df = pd.read_csv("data.csv",index_col="Name")

# SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())

# SELECTION BY COLUMN
# print(df[["Name","Height","Weight"]].to_string())

# SELECTION BY ROW/S
# print(df.loc["Charizard":"Blastoise",["Height","Weight"]])
# print(df.iloc[0:11])
# print(df.iloc[0:11:2])
# print(df.iloc[0:11:2,0:3])

# EXERCISE
pokemon = input("Enter Pokemon Name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not in DataFrame")