import matplotlib.pyplot as plt
import numpy as np

# scatter graph = Shows the relationship between two variables
#                 Helps to identify a correlation(+,-,None)
#                 Example : Study hours VS. test scores

x = np.array([0,1,1,2,3,4,5,6,7,7,8]) #Hours studied
y = np.array([55,60,65,62,68,70,75,78,82,85,87]) #Grades

x1 = np.array([10,11,11,12,13,14,15,16,17,17,18]) #Hours studied
y1 = np.array([90,45,66,67,68,70,75,78,82,85,87]) #Grades

plt.scatter(x, y,color = "red",alpha = 0.5,s = 100,label = "Class = A")
plt.scatter(x1, y1,color = "black",alpha = 0.5,s = 100,label = "Class = B")

plt.title("Test score")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.legend()
plt.show()