#Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.
import numpy as np

try:
    # Take input from user
    a = int(input("Enter number of rows (a): "))
    b = int(input("Enter number of columns (b): "))

    if a <= 0 or b <= 0:
        print("Both a and b must be positive integers.")
    else:
        # Generate a random array of shape (a, b)
        array = np.random.rand(a, b)  # values between 0 and 1

        # Print the array
        print("\nGenerated Random Array:")
        print(array)

        # Calculate and print the average
        average = np.mean(array)
        print(f"\nAverage of all elements: {average:.4f}")

except ValueError:
    print("Invalid input! Please enter valid integers.")
