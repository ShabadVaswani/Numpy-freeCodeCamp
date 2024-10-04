import numpy as np
a = np.array([1,2,3])
a1 = np.array(['1','2','3'])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)

b = a*np.array([1,3,5])

print(b)

l = a + np.array([7])

print(l) #=>This method is called broadcasting

l = a * np.array([7])

print(l) #=>This method is called broadcasting


sum1 = a * b
dot = np.sum(sum1)
print(dot) #=>This is dot product

dot = a @ b
print(dot) #=>This is dot product new syntax

a2 = np.array([[1,2,3],[5,7,8]])
print(a2[0]) #=>This is to get entire row
print(a2[:,2]) #=>This is to get entire column