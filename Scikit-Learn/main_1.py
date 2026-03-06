import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
print(x)

y = np.array(2*x)
print(y)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()

plt.scatter(x, y)
plt.show()