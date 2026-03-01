import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index,type_count,color='green',edgecolor='black')

plt.title("NO. of pokemon by primary type")
plt.xlabel("primary type")
plt.ylabel("count")

plt.tight_layout()
plt.show()