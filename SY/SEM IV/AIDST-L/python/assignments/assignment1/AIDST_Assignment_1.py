# Q1

import numpy as np
rand_num = np.random.normal(0,1,15)
print("15 random numbers from a standard normal distribution:")
print(rand_num)

# Q2


m= np.arange(10,22).reshape((3, 4))
print(m)

# Q3

x = np.array([[0,1],[2,3]])
print("Original array:")
print(x)
print("Sum of all elements:")
print(np.sum(x))
print("Sum of each column:")
print(np.sum(x, axis=0))
print("Sum of each row:")
print(np.sum(x, axis=1))