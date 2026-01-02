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
ans = 'No'
n = inp()
Hlist = inpl()
i = n-1
while i:
    if Hlist[i-1] >= Hlist[i]+2: 
        ans = 'No'
        break
    elif Hlist[i-1] == Hlist[i]+1:
        Hlist[i-1] = Hlist[i]
    i += -1

if i == 0: ans = 'Yes'

print(ans)