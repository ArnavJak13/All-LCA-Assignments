
# Assignment 4:
# Write a python program to create an array and perform addition of two matrices (Using list and numpy array)

# Matrix addition using Python lists
# Create two matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [10, 11, 12]]

# Create an empty result matrix
result = [[0, 0, 0], [0, 0, 0]]

# Add the matrices
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

# Display the result
print("Matrix addition using Python lists")
print("\nMatrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nAddition of matrices:")
for row in result:
    print(row)



# Matrix addition using Numpy lists
import numpy as np

# Create two NumPy arrays
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

# Add the matrices
result = A + B

# Display the matrices
print("\nMatrix addition using Numpy lists")
print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition of matrices:")
print(result)