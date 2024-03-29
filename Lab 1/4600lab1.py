import numpy as np
import numpy.linalg as la
import math


#Driver function helps call the functions previously implemented
def driver():
    n = 100
    x = np.linspace(0, np.pi, n)

    f = lambda x: np.cos(x)
    g = lambda x: np.cos(2 * x)
    y = f(x)
    w = g(x)

    # evaluate the dot product of y and w
    dp = dotProduct(y, w, n)
    # print the output
    print('The dot product is:', dp)
    return


#dot product function computes dot product of vectors x, y with dim n x 1
def dotProduct(x, y, n):
    dp = 0
    for j in range(n):
        dp = dp + x[j] * y[j]
    return dp


A = np.array([[1, 2, 3, 4], [4, 5, 4, 10]])
x = np.array([1, 2, 10, 35])


#Computes matrix vector multiplication for matrix A of size m x n and vector x of size n x 1
def matrixVectorProduct(A, x):
    if A.shape[1] != x.shape[0]:
        print('Incompatible System')
        return -1

    b = np.zeros([A.shape[0], 1])
    for i in range(A.shape[0]):
        b[i] = dotProduct(A[i], x, A.shape[1])
    return b


#Computes value of matrix multiplication through the default NumPy function
print(np.matmul(A, x))

#Compares value of my mat mul funciton to the numpy version to test correctness
print(matrixVectorProduct(A, x))


# driver()
