from mean_var_std import calculate
import json

# Test the function with the example from the requirements
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print("Result for [0,1,2,3,4,5,6,7,8]:")
print(json.dumps(result, indent=2))

print("\n" + "="*50 + "\n")

# Test with another example
result2 = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Result for [1,2,3,4,5,6,7,8,9]:")
print(json.dumps(result2, indent=2))

print("\n" + "="*50 + "\n")

# Test error case
try:
    calculate([1, 2, 3, 4, 5])
except ValueError as e:
    print(f"Error case (list with 5 elements): {e}")

print("\n" + "="*50 + "\n")

# Test the matrix structure
import numpy as np
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
matrix = np.array(test_list).reshape(3, 3)
print("The 3x3 matrix from [0,1,2,3,4,5,6,7,8]:")
print(matrix)
print("\nRows:")
for i, row in enumerate(matrix):
    print(f"Row {i}: {row}")
print("\nColumns:")
for i in range(3):
    print(f"Column {i}: {matrix[:, i]}")
