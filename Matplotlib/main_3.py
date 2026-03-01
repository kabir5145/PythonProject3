import matplotlib.pyplot as plt
import numpy as np

X = np.array([2023,2024,2025,2026])
Y1 = np.array([15,25,30,20])
Y2 = np.array([17,23,38,5])
Y3 = np.array([10,20,30,40])

plt.title("Class size",fontsize = 20,family = "Times New Roman",color = "blue")

plt.xlabel("Year",fontsize = 20,family = "Times New Roman",color = "blue")

plt.ylabel("Students",fontsize = 20,family = "Times New Roman",color = "blue")

plt.tick_params(axis='both', which='major', labelsize=20)

plt.plot(X,Y1)
plt.plot(X,Y2)
plt.plot(X,Y3)

plt.xticks(X)

plt.show()