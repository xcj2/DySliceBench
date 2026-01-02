import math
import functools
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
A = IL()

A.sort()
ABS = []
for i in range(1,N):
    ABS.append(A[i]-A[i-1])

ABS.sort()
num = A[1]
cnt = 0
for i in range(num+1,0,-1):
    cnt = 0
    for j in range(N):
        if A[j]%i==0:
            continue
        else:
            cnt += 1
        if cnt == 2:
            break
    else:
        print(i)
        exit()