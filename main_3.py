import numpy as np

# Slicing
array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

# for i in range(4):
#     for j in range(4):
#         print(array[i][j],end=" ")
#     print()

# array[start:end:step]
# print(array[0]) #[1,2,3,4]
# print(array[1]) #[5,6,7,8]
# print(array[2]) #[9,10,11,12]
# print(array[3]) #[13,14,15,16]
# print(array[-1]) #[13,14,15,16]


# print(array[1:4])

# print(array[0:4:2])
# print(array[::-1])
# print(array[::-2])

# print(array[:,0]) #[1,5,9,13]
# print(array[:,1]) #[2,6,10,14]
# print(array[:,2]) #[3,7,11,15]
# print(array[:,3]) #[4,8,12,16]

# print(array[:,1:4])
# print(array[2:,2:4])