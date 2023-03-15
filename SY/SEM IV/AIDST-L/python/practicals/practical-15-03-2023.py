# write a numpy program to create an array of 20 random numbers from a standard normal distribution
# write a numpy program to create a 3x4 matrix filed with values from 10 to 21
# wanp to compute sum of all elements, sum of each column and sum of each row of a given array

import numpy as np

arr = np.random.normal(0, 0.1, 20)
print(arr)

matrix = np.arange(10, 22).reshape(3,4)
print(matrix)

x = np.array([[0,1],[2,3]])
print("Original array:", x)
print("Sum of all elements:", np.sum(x))
print("Sum of each column:", np.sum(x, axis=0))
print("Sum of each row:", np.sum(x, axis=1))


elementno = int(input("Enter the number of elements you want array to be:"))
arr2 = np.random.normal(0, 0.1, elementno)
print(arr2)

#  wanp to compute multiplication of two matrices
# wanp to compute to compute cross product of two vectors
a = np.ones([9, 5, 7, 4])
c = np.ones([9, 5, 4, 3])
np.dot(a, c).shape
mm = np.matmul(a, c).shape
print(mm)

x = [1, 2, 3]
y = [4, 5, 6]
cp = np.cross(x, y)
print(cp)