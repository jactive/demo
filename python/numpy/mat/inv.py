import numpy as np
a = np.matrix([[1,2,], [3,4]])
b = a ** -1
c = np.linalg.inv(a)
print b
print a * b
print
print c
print a * c

