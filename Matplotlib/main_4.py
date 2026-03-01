import matplotlib.pyplot as plt
import numpy as np

# grid() = Helps make plots easier to read by adding reference lines.

x = np.array([1,2,3,4,5])
y = np.array([4,5,6,7,8])

# plt.grid(axis="x")
plt.grid(axis="y",linestyle="--")
plt.plot(x,y)
plt.show()