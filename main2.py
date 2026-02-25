import numpy as np
# Introduction to multidimensional arrays

# This is a 2-D Array
# array = np.array([['a', 'b', 'c'],
#                   ['d', 'e', 'f'],
#                   ['g', 'h', 'i']])

array = np.array([[['A','B', 'C'], ['D','E','F'], ['G','H','I']],
                  [['J','K','L'],['M','N','O'], ['P','Q','R']],
                  [['S','T','U'], ['V','W','X'], ['Y','Z',' ']],])

# print(array)
# print(array[0][0][0]) # chain indexing
# print(array.ndim)
# print(array.shape)

print(array[1][0][1],   # K
      array[0][0][0],   # A
      array[0][0][1],   # B
      array[0][2][2],   # I
      array[1][2][2],   # R
      sep="")