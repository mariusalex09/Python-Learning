import numpy as np

a = np.array([1, 2, 3])
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

print(b)
#get dimension with ndim
print(a.ndim)  #1
print(b.ndim)  #2

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

