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


n = inp()
Alist = inpl()
Blist = inpl()
Clist = inpl()

ans = 0

for i in range(len(Alist)-1):
    if Alist[i+1] == Alist[i]+1:
        ans += Clist[Alist[i]-1]
ans += sum(Blist)

print(ans)