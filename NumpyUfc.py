import numpy as np

"""
ufuncs are universal functions in Numpy that operates with ndarrays object
ufuncs are used to implement vectorization in numpy which is way faster than iterating over elements
ufuncs tak additional arguments like:
where - boolean array or condition defining where the operations should take place
dtype - defining the return type of elements
out - Output array where the return value should be copied
Vectorization is converting iterative statements into a vector based operation. it is faster and modern CPUs are optimized for such operations
"""

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = np.add(x, y)
print(z) # [ 6  8 10 12]



