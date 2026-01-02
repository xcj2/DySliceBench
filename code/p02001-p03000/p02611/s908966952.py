MOD=10**9+7

def matmul(A,B): # A,B: 行列
    res = [[0]*len(B[0]) for _ in [None]*len(A)]
    for i, resi in enumerate(res):
        for k, aik in enumerate(A[i]):
            for j,bkj in enumerate(B[k]):
                resi[j] += aik*bkj
                resi[j] %= MOD
    return res

def matpow(A,p): #A^p mod M
    if p%2:
        return matmul(A, matpow(A,p-1))
    elif p > 0:
        b = matpow(A,p//2)
        return matmul(b,b)
    else:
        return [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]

def solve(n):
    pass
# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

#n,k,*a = map(int,read().split())

T, = map(int,readline().split())


c = [1, -11, 50, -110, 65, 253, -648, 440, 610 , -1430 ,+ 780 ,+ 780, - 1430 ,  610 , 440, - 648, + 253, + 65, - 110, + 50, - 11, + 1]

m = 21
A = [[0]*m for _ in range(m)]
for i in range(m-1):
    A[i+1][i] = 1
for i in range(m):
    A[i][-1] = -c[i]
    
#print(A)


v = [[0]*(m-1)+[1]]
c = matmul(v,matpow(A,15))

#print(c)

for _ in range(T):
    n, = map(int,readline().split())
    x = matmul(c,matpow(A,n))
    print(x[0][0])

