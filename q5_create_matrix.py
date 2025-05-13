#Create a 5x5 matrix with row values ranging from 0 to 4.

import numpy as np

# Create a 5x5 matrix with row values ranging from 0 to 4
matrix = np.arange(5).reshape(1, 5).repeat(5, axis=0)
print(matrix)
