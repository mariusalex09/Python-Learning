import numpy as np

a = np.array([1, 2, 3])
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

print(b)
#get dimension with ndim
print(a.ndim)  #1
print(b.ndim)  #2
arr = np.array([1,2,3,4], ndmin = 5)
"""
[[[[[1 2 3 4]]]]]
"""
print(arr.shape) #(1,1,1,1,4)

#get shape with shape
print(a.shape)  #(3,)
print(b.shape)  #(2, 3)

#get datatype with dtype
print(a.dtype)  #int32
print(a.itemsize)  #4 bytes
print(b.dtype)  #float64

a = np.array([1, 2, 3], dtype='int16')
print(a.dtype)  #int16
print(a.itemsize)  #2 bytes
print(b.itemsize)  #8

#Accessing/changing secific elements, rows, columns, etc
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a.shape)  #(2, 7)

#get specific element [r, c]
print(a[1, 5])  #13
print(a[1, -2])  #13

#get specific row
print(a[0, :])  #[1 2 3 4 5 6 7]
#get specific column
print(a[:, 2]) # [ 3, 10]

#get little more fancy [startindex:stopindex:stepsize]
print(a[0, 1:6:2])  #[2, 4, 6]

#change
a[1, 5] = 20
print(a)
#[[ 1  2  3  4  5  6  7]
# [ 8  9 10 11 12 20 14]]

a[:, 2] = 5 #change on column 3 for al lines to value 5
print(a)
#[[ 1  2  5  4  5  6  7]
# [ 8  9  5 11 12 20 14]]
 
a[:, 2] = [1, 2] # change on all lines the values on column 3 with 1 and 2
print(a)

#3d examples

b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
"""
[[[1 2]     < first part
  [3 4]]

 [[5 6]     < second part
  [7 8]]]
"""

#get element (work outside in)
print(b[0,1,1]) # gets 4
print(b[:,0, 0])

#replace
b[:, 1, :] = [[9, 9], [8, 8]]
print(b)
"""
[[[1 2]
  [9 9]]

 [[5 6]
  [8 8]]]
"""

#initialiye different types of arrays
#all 0's matrix
a = np.zeros(5)
print(a) # [0. 0. 0. 0. 0.]

a = np.zeros((2, 3))
print(a)
"""
[[0. 0. 0.]
 [0. 0. 0.]]
"""

#all 1's matrix
a = np.ones((4,2,2), dtype='int32')
print(a)
"""
[[[1 1]
  [1 1]]

 [[1 1]
  [1 1]]

 [[1 1]
  [1 1]]

 [[1 1]
  [1 1]]]
"""

#any other number
a = np.full((2, 2), 99)
print(a)
"""
[[99 99]
 [99 99]]
"""

#any other number (full_like)
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
b = np.full_like(a, 4)
print(b)
"""
[[4 4 4 4 4 4 4]
 [4 4 4 4 4 4 4]]
"""

#initialize an array of decimal numbers
a = np.random.rand(4, 2)
print(a)
"""
[[0.49378482 0.1988482 ]
 [0.36015859 0.4209432 ]
 [0.85529089 0.43308431]
 [0.63987565 0.58510908]]
"""

b = np.random.random_sample(a.shape)
print(b)
"""
[[0.04707599 0.63128806]
 [0.75159586 0.85252538]
 [0.88637604 0.97621766]
 [0.80636512 0.46929374]]
"""

#random integer values
a = np.random.randint(-4, 7, size = (3, 3))  #randomizes between -4 and 7 
print(a)
"""
[[-1  3  0]
 [ 0  2 -3]
 [ 6  0 -2]]
"""

#identity matrix
a = np.identity(5)
print(a)
"""
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
"""

arr = np.array([1,2,3])
a = np.repeat(arr, 3)
print(a) #[1 1 1 2 2 2 3 3 3]

#repeat an array
arr = np.array([[1,2,3]])
print(arr) # [[1 2 3]]
a = np.repeat(arr, 3, axis = 0)
print(a)
"""
[[1 2 3]
 [1 2 3]
 [1 2 3]]
"""

""" build an array like:
1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1 
"""
a = np.ones((5,5), dtype='int16')
z = np.zeros((3, 3))
z[1, 1] = 9
a[1:4, 1:4] = z
print(a)
"""
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 9 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
"""

#Mathematics
a = np.array([1,2,3,4])

print(a + 2) #[3 4 5 6]
print(a - 2) #[-1  0  1  2]
print(a * 2) #[2 4 6 8]
print(a / 2) #[0.5 1.  1.5 2. ]

b = np.array([1,0,1,0])
print(a + b) # [2 2 4 4]

print(np.sin(a))  # [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]

#Linear algebra
a = np.ones((2,3))
b = np.full((3,2), 2)
print(a,b)
"""
[[1. 1. 1.]
 [1. 1. 1.]]
 and
 [[2 2]
 [2 2]
 [2 2]]
"""

print(np.matmul(a,b))
"""
[[6. 6.]
 [6. 6.]]
"""

c = np.identity(3)
print(c)
"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""
#linear algebra more on https://numpy.org/doc/stable/reference/routines.linalg.html
print(np.linalg.det(c))  #1.0

#statistics
stats = np.array([[1,2,3], [4,5,6]])
min = np.min(stats) #1
max = np.max(stats )#6
print(np.min(stats, axis=0))  #[1,2,3]
print(np.min(stats, axis=1))  #[1,4]
print(np.max(stats, axis=0))  #[4,5,6]
print(np.max(stats, axis=1))  #[3,6]
print(np.sum(stats)) #21
print(np.sum(stats, axis=0)) #[5,7,9]

#reorganizing arrays
before = np.array([[1,2,3,4], [5,6,7,8]])
print(before.shape)  #[2,4]

after = before.reshape(8,1)
print(after)
"""
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]]
"""

#vertically stacking vectors
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
"""
[[1 4]
 [2 5]
 [3 6]]
"""


v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))
"""
[[1 2 3 4]
 [5 6 7 8]]
"""
print(np.vstack([v1,v2,v2,v2]))
"""
[[1 2 3 4]
 [5 6 7 8]
 [5 6 7 8]
 [5 6 7 8]]
"""
#horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(np.hstack([h1,h2]))
"""
[[1. 1. 1. 1. 0. 0.]
 [1. 1. 1. 1. 0. 0.]]
"""

#dstack() to stack along height, which is the same as depth.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)
"""
[[[1 4]
  [2 5]
  [3 6]]]
"""

#Load data from a file
filedata = np.genfromtxt('dataNumpy.txt', delimiter = ',')
print(filedata)
"""
[[  1.  13.  21.  11. 196.  75.   4.   3.   4.   7.   8.   0.   1.  23.]
 [  3.  42.   5.  65.  89.   7.  55.  90.   0.  12.  11.  45.  13.  14.]
 [  1.  22.  23.  56.  45.  10.  89.  98.  77.  46.   2.   3.   5.   6.]]
"""
fnew = filedata.astype('int32')
print(fnew)
"""
[[  1  13  21  11 196  75   4   3   4   7   8   0   1  23]
 [  3  42   5  65  89   7  55  90   0  12  11  45  13  14]
 [  1  22  23  56  45  10  89  98  77  46   2   3   5   6]]
"""

#Advanced indexing and boolean masking
print(fnew > 50)
"""
[[False False False False  True  True False False False False False False
  False False]
 [False False False  True  True False  True  True False False False False
  False False]
 [False False False  True False False  True  True  True False False False
  False False]]
"""

print(fnew[fnew > 50])
"""
[196  75  65  89  55  90  56  89  98  77]
"""
#you can index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]]) #[2,3,9]

print(np.any(fnew > 50, axis = 0))   #axis = 0 means column and axis = 1 means row
"""
[False False False  True  True  True  True  True  True False False False
 False False]
"""
print(np.any(fnew > 50, axis = 1))
"""
[ True  True  True]
"""

#similarly can use np.all when all values  must match a condition e.g. print(np.all(fnew > 50, axis = 1))
print((fnew > 50) & (fnew < 100))
"""
[[False False False False False  True False False False False False False
  False False]
 [False False False  True  True False  True  True False False False False
  False False]
 [False False False  True False False  True  True  True False False False
  False False]]
"""

#get the opposite by using ~ sign
print(~((fnew > 50) & (fnew < 100)))
"""
[[ True  True  True  True  True False  True  True  True  True  True  True
   True  True]
 [ True  True  True False False  True False False  True  True  True  True
   True  True]
 [ True  True  True False  True  True False False False  True  True  True
   True  True]]
"""

#exercise
p = np.array(range(1,31))
print(p) 
"""
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
 25 26 27 28 29 30]
"""
new_p = p.reshape(6,5)
print(new_p)
"""
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]
 [26 27 28 29 30]]
"""

#get 11,12,16,17
new_p[2:4, 0:2]
#get 2,8,14,20
new_p[[0,1,2,3], [1,2,3,4]]
#get 4,5  24,25, 29,30
new_p[[0,4,5], 3:]


#Numpy arrays can have different datatypes as inhttps://www.w3schools.com/python/numpy/numpy_data_types.asp
#can be interger, unsigned, float, datemtime, string, unicode string and many more

#advanced iteration through arrays with nditer
arr = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
#normal iteration using for loop
for x in arr:
    for y in x:
        for z in y:
            print(z)  # would list all elements one by one

for x in np.nditer(arr):
    print(x) # will do the same as example above

arr = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr[:, ::2]):
    print(x) # will print 1 3 5 7

#np.ndenumerate
arr = np.array([1,2,3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
"""
(0,) 1
(1,) 2
(2,) 3
"""
arr = np.array([[1,2,3,4], [5,6,7,8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
"""
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8
"""

#ARRAYS JOIN
a = np.array([1,2,3])
b = np.array([4,5,6])

arr = np.concatenate((a, b))  #[1,2,3,4,5,6]
print(arr)

#Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis = 1)
print(arr)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""
arr = np.concatenate((arr1, arr2), axis = 0)
print(arr)
"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

#ARRAY SPLIT
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 3)
print(newarr)
""""
[array([1, 2]), array([3, 4]), array([5, 6])] #it is in fact a list
"""
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr, 4)  #if array has less elements than required, it adjusts from the end accordingly
print(newarr)  #[array([1, 2]), array([3, 4]), array([5]), array([6])]

#split 2D arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
"""
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])]
"""

#split 2D array along row
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis = 1)
print(arr)
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]
 [13 14 15]
 [16 17 18]]
"""
print(newarr)
"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""

#or can use hsplit which is opposite to hstack
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""
#ARRAY SEARCH
#search array for a certain value and return the indexes that get a match - use where() method
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print(x) #(array([3, 5, 6], dtype=int64),)
x = np.where(arr % 2 == 0)
print(x) #(array([1, 3, 5, 6], dtype=int64),)

#searchsorted() method is assumed to be used on sorted arrays - always
arr = np.array([6,7,8,9])
x = np.searchsorted(arr, 7)
print(x) #returns 1 as it is the index where value 7 could be inserted so that order remains
x = np.searchsorted(arr, 7, side = 'right') #can search from right too
print(x) #2

#search for multiple values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
"""
[1 2 3]
"""
#ARRAY SORT
arr = np.array([3,2,0,1])
sorted_arr = np.sort(arr)
print(sorted_arr) #[0 1 2 3]

#can sort also array of strings
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr)) #['apple' 'banana' 'cherry']

#sorting on 2D arrays-> will sort both arrays
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) 
"""
[[2 3 4]
 [0 1 5]]
"""

#ARRAY FILTER
arr = np.array([41,42,43,44])
x = [True, False, False, True]
print(arr[x]) #[41 44]

a = np.array([1,2,3,4,5,6,7,8,9])
b = a > 5
print(b) #[False False False False False  True  True  True  True]
print(a[b]) #this is direct filter and filters in only elements greater than 5 [6 7 8 9]
print(a[a%2 == 0]) # [2 4 6 8]