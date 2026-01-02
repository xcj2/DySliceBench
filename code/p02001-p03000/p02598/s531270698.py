import os
import sys
import math
import heapq
from decimal import *
from io import BytesIO, IOBase
from collections import defaultdict, deque

def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))
def chk(mid,a,n,k):
    cuts=0
    for i in a:
        if i <= mid:
            continue
        cuts += i//mid+(-1 if i%mid==0 else 0)
    return (True if cuts<=k else False)

n,k = rm()
a = rl()
lo = 1
hi = 10**9
ans = 10**9
while lo < hi :
    mid = (lo+hi)//2
    if chk(mid,a,n,k):
        hi=mid
        ans=mid
    else:
        lo = mid+1
print(ans)