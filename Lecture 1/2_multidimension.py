import numpy as np

a = np.array([[1,2],[5,7]])
print(a[0]) #=>This is to get entire row
print(a[:,1]) #=>This is to get entire column

print(a.T) #=>This is to Transpose

print(np.linalg.inv(a)) #=>This is to get inverse
print(np.linalg.det(a)) #=>This is to get determinant



