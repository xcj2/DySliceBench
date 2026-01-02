from collections import defaultdict,deque, Counter
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
ans = 1

[n,m] = inpl()
fibsec = [0]*(n+2)
fibsec[0] = 1
fibsec[1] = 1
fibsec[-1] = 0
for i in range(2,n+1):
    fibsec[i] = fibsec[i-1]+fibsec[i-2]

firsta = -1
for k in range(m):
    seconda = inp()
    ans = ans*(fibsec[seconda-firsta -2 ])%mod
    firsta = seconda

ans = ans*(fibsec[n-firsta-1])%mod
    

print(ans)