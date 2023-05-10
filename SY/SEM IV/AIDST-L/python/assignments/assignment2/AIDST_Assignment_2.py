# Q1

import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the said matrix multiplication:")
print(result1)

# Q2

p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)

# Q3

m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result =  np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)

# Q4

m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Condition number of the said matrix:")
print(result)