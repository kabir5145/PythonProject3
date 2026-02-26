import numpy as np

# Arithmetic

# Scalar arithmetic

# array = np.array([1,2,3])

# print(array + 1)
# print(array - 2)
# print(array * 2)
# print(array / 2)
# print(array // 2)
# print(array ** 2)

# Vectorized math function
# array = np.array([1.01,2.5,3.99])

# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array)) #always round down
# print(np.ceil(array)) #always round up
# print(np.pi)

#EXERCISE
# radii = np.array([1,2,3])
# print(np.pi*radii**2)

# Element-wise arithmetic
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 // array2)
# print(array1 % array2)
# print(array1 ** array2)

# Comparison operators
scores = np.array([99,87,65,54,100])
print(scores == 100)
print(scores <60)

scores[scores >= 60] = 99
print(scores)