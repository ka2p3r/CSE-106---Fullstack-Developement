#2a. Using numpy operation to calc matrix
import numpy as yeet
a = yeet.arange(1, 10).reshape(3, 3)
b = yeet.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])
print(yeet.add(a, b))

print('------------------------------------------')

#2b. Multiplication
print(yeet.multiply(a, b))

print('------------------------------------------')

#2c. Finding the determinate of a
det = yeet.linalg.det(a)
print(yeet.round(det))

print('------------------------------------------')

#2d. Finding the inverse of b
inv = yeet.linalg.inv(b)
print(inv)

print('------------------------------------------')

#2e. Finding the eigenvalues of A
e, v = yeet.linalg.eig(a)
print(e)