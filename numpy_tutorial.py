import pandas as pd
import numpy as np

#using Numpy

number = np.array([[1,2,3],#0
                   [4,5,6],#1
                   [6,8,9],#2
                   [3,6,1] #3
                   ])
print(number.shape)
print(number.size)
print(number.ndim)

print(number.dtype)
print(number[:2,2:])
number[2]=99
print(number)

#scaling an vectorization of matrices
num = np.array([[1,2,3],#0
                   [4,5,6],#1
                   [6,8,9],#2
                   [3,6,1] #3
                   ])
print(num.sum(axis=0))
print(num.sum(axis=1))
print(num.mean(axis=0))
print(num.mean(axis=1))
print(num.sum())
print(num.std())
print(num.mean())
print(num.var())

#boolean arrays

a = np.arange(4)

print("The array from index 0 to 3 is : ",a)
print("The value of index [0] and index [3] is : ",a[[0, -1]])
print("Selecting elements using boolean hence the true values displays : ",a[[True,False,False,True]])
print("Finding the corresponding truth value of the condition a>=2 : ",a>=2)
print(" The mean value of the array is : ",a.mean())
print("The value of the condition a>=2 are: ", a[a>=2])
print(a[(a == 0)|(a == 1)])


A =np.random.randint(100, size=(3,3))
print(A)

#linear algebra

a = np.array([[1,2,3],#0
                   [4,5,6],#1
                   [6,8,9],#2
                   [3,6,1] #3
                   ])

b = np.array([[1,2, 3],
              [4 ,5 ,6],
              [3 ,6 ,1]])

print("The multiplication of array a and array b is  : ",a.dot(b)#or print(a@b)
      )
print(b.T)
