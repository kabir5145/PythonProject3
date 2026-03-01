import matplotlib.pyplot as plt
import numpy as np

X = np.array([2023,2024,2025,2026])
Y1 = np.array([15,25,30,20])
Y2 = np.array([17,23,38,5])
Y3 = np.array([10,20,30,40])

line_style = dict(marker='o',markersize=10, markerfacecolor='red',markeredgecolor='red',
                  linestyle='dashdot',linewidth=2)


plt.plot(X,Y1,color = "green", **line_style)
plt.plot(X,Y2,color = "black", **line_style)
plt.plot(X,Y3,color = "orange", **line_style)

plt.show()