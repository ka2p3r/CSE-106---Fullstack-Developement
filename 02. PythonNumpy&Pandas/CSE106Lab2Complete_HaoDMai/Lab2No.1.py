#CSE 106 Lab no.2
# Exploration and implementation of numpy and pandas
import numpy as yeet


#1. Create and print 4*2 matrix values from 2 to 10
var = yeet.arange(2,10).reshape(4,2)
print(var)

print('------------------------------------------')


#1b. Print a 8*8 matrix in a checkerboard pattern
var1 = yeet.zeros((8,8), dtype=int) #.zero function in numpy allows for matrix creation and declaring data type
# manipulation of row's and column index to resemble checkered pattern
var1[1::2, ::2] = 1
var[::2, 1::2] = 1
print(var1)

print('------------------------------------------')


#1c. By creating a list, employing the numpy function .unique will discard redundancy and spit out single values
l = [10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
print(yeet.unique(l))

print('------------------------------------------')


#1d. using numpy function to find a desired value from a list of number
# numpy may only work with array
z = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
#convert the list to an array
y = yeet.array(z)
# to find the value that is greater than 37 base on numpy syntax
v = y[y > 37]
print(v)

print('------------------------------------------')


#1e. using numpy function to implement temperature conversion formula from C into F
t = [0, 12, 45.21, 34, 99.91]
T = yeet.array(t)
#plugging the vairbale within the array into conversion formula
print(yeet.round((9*(T)/5 + 32), 2))

print('------------------------------------------')
