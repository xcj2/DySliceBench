from enum import Enum
from queue import Queue
import collections

import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

def partition(A,p,r):
    i = p-1
    for j in range(p,r):
        if A[j][1]<=A[r][1]:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def QuickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

def isStable(A):
    for i in range(1,len(A)):
        if A[i-1][1] == A[i][1]:
            if A[i-1][2] > A[i][2]:
                return 'Not stable'
    return 'Stable'

n = int(input())
A = []
for i in range(n):
    suit,num = sys.stdin.readline().split()
    A += [[suit,int(num),i]]
QuickSort(A,0,n-1)
print(isStable(A))
for i in A:
    print(i[0],i[1])

