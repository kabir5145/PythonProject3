import numpy as np

# Aggregate functions = summarize data and typically return a single value

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
# print(np.sum(array)) #Sum of whole array
# print(np.mean(array)) #Average
# print(np.std(array)) #Standard deviation
# print(np.var(array)) #Variance
# print(np.median(array)) #Median
# print(np.min(array)) #Minimum value
# print(np.max(array)) #Maximum value
# print(np.argmin(array)) #Position of the minimum value
# print(np.argmax(array)) #Position of the maximum value

print(np.sum(array,axis=0)) #Applying sum to the columns
print(np.sum(array,axis=1)) #Applying sum to the rows