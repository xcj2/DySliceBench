
import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline




def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())

directions=np.array([[1,0],[0,1],[-1,0],[0,-1]])
directions = list(map(np.array, directions))

mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

res=[]
def search(seq,k,n):
    global N
    
    if k==N+1:

        tmp=[ascii_lowercase[s-1] for s in seq[1:]]
        res.append("".join(tmp))
        return 
    
    seq[k]=n
    search(seq,k+1,n+1)
    
    for l in range(1,n):
        seq[k] = l
        search(seq, k+1,n)
    

def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return int(result)


def nCr(n, r):
    """
    Calculate the number of combination (nCr = nPr/r!).
    The parameters need to meet the condition of n >= r >= 0.
    It returns 1 if r == 0, which means there is one pattern
    to choice 0 items out of the number of n.
    """

    # 10C7 = 10C3
    r = min(r, n-r)

    # Calculate the numerator.
    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i

    # Calculate the denominator. Should use math.factorial?
    denominator = 1
    for i in range(r, 1, -1):
        denominator *= i

    return numerator // denominator


N=int(input())
A=acinput()


y=[0]*(max(A)+1)
for i in range(N):
    y[A[i]]+=1

cb=[0]*len(y)

b=0
for i in range(1,len(y)):
    if y[i] >= 2:
        cb[i]=cmb(y[i],2)
    
        b+=cb[i]
    
for i in range(N):
    k=A[i]
    #print(i,k,y)
    tmp=0
    if y[k]-1>=2:
        tmp = nCr(y[k]-1, 2)
    tmp2=b-cb[k]+tmp
    #print("y",y[k],nCr(y[k]-1, 2))
    print(tmp2)
    
#print(cb)
    
#print(y)
#print(b)

