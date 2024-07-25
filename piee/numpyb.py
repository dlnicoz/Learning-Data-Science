import numpy as np

# arr = np.array([1,3,4,5,6])
# print(arr)
# ty = type(arr)
# print(ty)

# 0d array
a = np.array(43)
# 1d array
b = np.array([1,2,3])
# 2d array 
c = np.array([[1,3,4] , [1,2,8]])
# 3d array
d = np.array([[[1,2,3],[1,2,4]],[[1,2,3] , [2,3,4]]])

# print(d)

# number of dimensions
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# array indexing
# print(b[2])
# accessinG 2D ARRAY
# print("THIS is 2d array", c[0,2])
# acceccing 2d array
# print("this is 3d array", d[0,1,2])

# array slicing
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr[2:4])
# print(arr[:4])
# print(arr[4:])
# print(arr[-4:-1])

# array datatypes
# arr = np.array([1,2,3,4] , dtype='S')
# print(arr.dtype)

# changing datatype  
# arr = np.array([1.2,-3.2,1.1])
# newarr = arr.astype(int)
# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)

# array Copy and View
# arr = np.array([1,3,4,5,3])
# x = arr.copy()
# arr[2] = 32
# x[0] =98
# print(arr , x)

# view
# arr = np.array([2,3,41,45])
# v = arr.view()
# print(arr  , v)
# arr[1] = 32
# print(arr , v)

# array shapes
# print(a, a.shape)
# print(b, b.shape)
# print(c, c.shape)
# print(d, d.shape)

# array reshape
# ab = b.reshape(2)
# bb = c.reshape(2,-1)
# bc = d.reshape(2,-1)

# print(ab)
# print(bb)
# print(bc)

# array iterating

# for x in b:
#     print(x)

# for x in d:
#     for y in x:
#         print(y) 

# array joining arrays 
aa = np.array([1,1,1,2])
ab = np.array([2,2,2,3])

# newa = np.concatenate([aa, ab])
# newa = np.stack((aa,ab) , axis=0)
# newa = np.hstack((aa,ab) )
# newa = np.vstack((aa,ab) )
# newa = np.dstack((aa,ab) )
# print(newa)

# array splitting

# newa = np.split(b, 3)
# newa = np.vsplit(d, 2)
# newa = np.hsplit(d, 2)
# print(newa)

# array searching

numb = np.array([21,34,12,45,76,43,67])
numc = np.array([11,14,42,55,76,43,67])
# res = np.where(numb > 45)
# res = numb.searchsorted([99,55])
# res = numb.argmax()
# res = numb.argmin()
# print(res)

# array sorting
# numb.sort
# res  = np.argsort(numb)
# print(res)

# array filtering

# condition = numb > 40
# print(condition)



