
import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)


def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())

mod = 10**9+7


def factorial(n):
    fact = 1
    for integer in range(1, n + 1):
        fact *= integer
    return fact


a,b,q=acinput()

S=[-10**15]
for i in range(a):
    S.append(II())
S.append(10**15)

T=[-10**15]
for i in range(b):
    T.append(II())
T.append(10**15)
X=[II() for i in range(q)]

import bisect


def near(arr,v):
    t=bisect.bisect(arr,v)
    
    #print(arr,v,t)
    if t>len(arr)-1:
        return len(arr)-1
    if t==0:
        return 0

    m = (abs(arr[t-1]-v) > abs(arr[t]-v))
    res = t+m-1
    #print(arr, v, res,m)
    return res


#print(S)
for i in range(q):
    x=X[i]

    s=bisect.bisect_right(S,x)
    t = bisect.bisect_right(T, x)
    res=10**19
    for ss in [S[s-1],S[s]]:
        for tt in [T[t-1],T[t]]:
            tmp=abs(ss-x)+abs(ss-tt)            
            res=min(res,tmp)
            tmp = abs(tt-x)+abs(ss-tt)
            res = min(res, tmp)
    print(res)


