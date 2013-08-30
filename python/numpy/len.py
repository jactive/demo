import numpy as np
a = np.array([1,2,3])
print a
print np.tile(a, 2)
a = np.tile(a, (2,3))
print a
print len(a);
print len(a[0]);
print a.shape
print len(a.shape) # dim
