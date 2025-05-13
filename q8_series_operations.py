# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd

# Create two Pandas Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([5, 10, 15, 20, 25])

# Perform addition
addition = series1 + series2
print("Addition of Series 1 and Series 2:")
print(addition)

# Perform subtraction
subtraction = series1 - series2
print("\nSubtraction of Series 1 and Series 2:")
print(subtraction)

# Perform multiplication
multiplication = series1 * series2
print("\nMultiplication of Series 1 and Series 2:")
print(multiplication)

# Perform division
division = series1 / series2
print("\nDivision of Series 1 by Series 2:")
print(division)
