from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

#n players, k points, q rounds
[n,k,q] = inpl()
pcount = defaultdict(int)
for _ in range(q):
    i = inp()
    pcount[i] += 1
    
for _ in range(1,n+1):
    print('Yes' if k-q+pcount[_]>0 else 'No')