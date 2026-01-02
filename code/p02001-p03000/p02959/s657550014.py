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

n = inp()
Alist = inpl()
Blist = inpl()
ans = 0
for i in range(n):
    ApA = Alist[i]+Alist[i+1]
    if Blist[i] >= ApA:
        ans += ApA
        Alist[i+1] = 0
    elif Blist[i] >= Alist[i] and Blist[i] <ApA:
        ans += Blist[i]
        Alist[i+1] = ApA - Blist[i]
    elif Blist[i] < Alist[i]:
        ans += Blist[i]

print(ans)