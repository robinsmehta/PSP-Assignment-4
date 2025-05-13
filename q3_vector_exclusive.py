# Create a vector of size 10 with values ranging from 0 to 1, both excluded.
import numpy as np

# Create a vector of size 10 with values in (0, 1)
vector = np.random.uniform(low=0.1, high=0.9, size=10)

# Print the vector
print("Vector with values between 0 and 1 (excluded):")
print(vector)
