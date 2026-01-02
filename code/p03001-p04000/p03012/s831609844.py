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
ans = 0

n = inp()
Wlist = inpl()
Wnplist = np.array(Wlist)

fullsum = Wnplist.sum()
halfsum = Wnplist.sum()//2
tempsum = 0
i= 0
while tempsum <= halfsum:
    tempsum += Wnplist[i]
    i += 1

i -= 1

ans1 = abs((fullsum - tempsum)-tempsum)
tempsum -= Wnplist[i]
ans2 = abs((fullsum - tempsum)-tempsum)

print(min(ans1,ans2))