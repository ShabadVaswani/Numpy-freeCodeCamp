import numpy as np


a = np.array([[1,2,3,4],[5,7,8,9]])
print(a[0,1:3]) #=>This is to get elements 1 to upto 2
print(a[:,1:3]) #=>This is to get columns 1 to upto 2

b = a[-1,-3] #third last element of last column
print(b)

#boolean indexing:

bool_idx = a>2
print(a[bool_idx]) #index where a>2 but it is not giving in 
