from __future__ import division, print_function
import sys
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
#from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return map(int if arg==0 else str,input().split())
#------------------------------------------------------------------


n,m,x = mapi()
a =[]
cost = []
for i in range(n):
    tmp = list(mapi())
    cost.append(tmp[0])
    a.append(tmp[1:])
#
res = 0
def check(y):
    for i in y:
        if i<x:
            return False
    return True

def rec(i,arr):
    if check(arr):
        return 0
    if i>=n:
        return float("inf")
    #res= float("inf")
    selct = a[i][:]
    for l in range(m):
        selct[l]+=arr[l]
    return min(cost[i]+rec(i+1,selct),rec(i+1,arr))
tm = [0]*m
res = rec(0,tm)
if res==float("inf"):
    print(-1)
else:
    print(res)
