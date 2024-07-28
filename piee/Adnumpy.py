import numpy as np

scalar = np.array(233)
# print("this is scalar :",scalar)

vector = np.array([23,45,235,65])
# print("this is vector :",vector)

matrix = np.array([[34,23,54,65],[43,65,23,54]])
# print("this is matrix :\n",matrix)

# 3d -----------

# ----type conversion

arr = np.array([1.3,54.5,65.2])
newarr = arr.astype(int) # str , int , bool , complex
# print(arr.dtype , newarr.dtype)

# can create np array with define datatypes
arra = np.array(['apple' , 'banana'], dtype='S')
# print(arra.dtype)

# -----Masking , filtering

arrm  = np.array([1,2,4,5,6,7,8])
# mask = arrm > 4
mask = arrm != 4 
# print(mask)  == >= <= !=

# to print those values
fil = arrm[mask]
# print(fil)

matrix2 = np.array([[1,2,3] , [4,4,5] , [3,6,6]])
# print("this is 2d array \n" , matrix2)


# array indexing
# print(matrix2[1,2])

# array slicing 
slc = matrix2[0:2, 0:2] 
# print("this is sliced matrix \n" , slc)

# ------slicing
ar = np.array([2,3,4,51,2])
# print(np.sort(ar))
# print(np.sort(matrix2 , axis=1))
# print(np.sort(matrix2 , axis=0))

# -------- array searching

asea = np.array([1,0,4,5,6])
index = np.where(asea >= 3)
# print(index , asea[index])

# broadcasting arithmetic on different arrays 
mul = arr + matrix2
# print(mul)

# vectorization 
# performing operations without explicit loops
arr = np.array([1,2,3,4])
varr = arr ** 2
# print(varr)

# shallow and copy
arrv = arr.view()
arrc = arr.copy()
print(arrv , arrc)
arrv[1] = 99 
# print("this is updateion" ,arrv , arrc)
# print(arr,arrv)

# stacking array
arrst = np.stack((arrv, arrc ) , axis=1)
print(arrst)
