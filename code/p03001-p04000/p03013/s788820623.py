import sys
sys.setrecursionlimit(10 ** 6)

from itertools import product

def mat2_mul(X, Y):
    Z = [ [0, 0], 
          [0, 0] ]
    for (i,j,k) in product(range(2),range(2),range(2)):
        Z[i][j] += X[i][k] * Y[k][j]
    return Z

def mat2_pow(X, n):
    if n == 0:
        return [ [1, 0],
                 [0, 1] ]
    elif n % 2:
        return mat2_mul(X, mat2_pow(X, n-1))  
    else:
        half_pow = mat2_pow(X, n/2)
        return mat2_mul(half_pow, half_pow)

def Fib(n):
    if n == 0:
        return 0
    else:
        F = [ [0, 1],
              [1, 1] ]
        return mat2_pow(F, n-1)[1][1]
    
    
N, M = map(int, input().split())
A = [int(input()) for i in range(M)]

x=0
L=[]
for i in range(M):
    L += [A[i] - 1 - x]
    x = A[i] + 1
L += [N - x]
L = [Fib(i+1)%1000000007 for  i in L]

X=1
for i in range(len(L)):
    X *= L[i]
    X %= 1000000007 
print(X)