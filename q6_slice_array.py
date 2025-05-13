#Write a program to input an array of numbers from the user (at least 10 elements in list), sort them and perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9. 

# Input 10 or more elements from the user
arr = list(map(int, input("Enter at least 10 numbers separated by spaces: ").split()))

# Check if the array has at least 10 elements
if len(arr) < 10:
    print("Please enter at least 10 elements.")
else:
    # Sort the array
    arr.sort()
    print("Sorted array:", arr)

    # Perform slicing operations
    slice_2_5 = arr[2:6]  # Elements between index 2 and 5 (inclusive)
    slice_5_8 = arr[5:9]  # Elements between index 5 and 8 (inclusive)
    slice_2_9 = arr[2:10]  # Elements between index 2 and 9 (inclusive)

    # Print the slices
    print("Elements between index 2 and 5:", slice_2_5)
    print("Elements between index 5 and 8:", slice_5_8)
    print("Elements between index 2 and 9:", slice_2_9)
