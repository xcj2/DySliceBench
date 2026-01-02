from enum import Enum
from queue import Queue
import collections

import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

def bubbleSort(A):
    count = 0
    for i in range(1,len(A)):
        for j in range(1,len(A)-i+1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                count += 1
    return A,count

def merge(A, left, mid, right):
    count = 0

    L = A[left:mid] + [BIG_NUM]
    R = A[mid:right] + [BIG_NUM]
    i = 0
    j = 0
    for k in range(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += len(L)-1-i
    return count

def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right)//2
        cnt1 = mergeSort(A, left, mid)
        cnt2 = mergeSort(A, mid, right)
        cnt3 = merge(A, left, mid, right)
        return cnt1+cnt2+cnt3
    else:
        return 0

n = int(input())
A = list(map(int,input().split()))
cnt=0
cnt = mergeSort(A,0,n)
#print(*A)
print(cnt)

