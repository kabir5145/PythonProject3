import numpy as np

# Random Numbers

# rng = np.random.default_rng()
# rng = np.random.default_rng(seed = 1)

# print(rng.integers(low = 1,high = 101,size = 3)) #size: 3 = Stored in 1D array
# print(rng.integers(low = 1,high = 101,size = (3,2))) #size : (3,2) = Stored in 2D array

# Floating point numbers
# np.random.seed(seed=1)
# print(np.random.uniform(low=0,high=10,size=10))

# Shuffle an array
rng = np.random.default_rng()

# array = np.array([1,2,3,4,5])
# rng.shuffle(array)

# print(array)

fruits = np.array(["apple", "banana", "cherry","coconut","pineapple"])
fruits = rng.choice(fruits,size=(3,3))
print(fruits)