# Create an array of random integer numbers as a numpy array, sort them and perform operations such as reshaping of the array into matrix of feasible dimensions. (e.g., if we have an array of 1 * 10, then we can reshape it into 2 * 5 or 5 * 2 matrix.) [Hint: Use the array of reshape (row * column)]

import numpy as np

# Create a random array of 10 integers between 1 and 100
arr = np.random.randint(1, 101, 10)

# Sort the array
sorted_arr = np.sort(arr)

print("Sorted array:", sorted_arr)

# Reshape the array into a 2x5 matrix or 5x2 matrix
reshaped_2x5 = sorted_arr.reshape(2, 5)
reshaped_5x2 = sorted_arr.reshape(5, 2)

print("Reshaped into 2x5 matrix:")
print(reshaped_2x5)

print("Reshaped into 5x2 matrix:")
print(reshaped_5x2)
