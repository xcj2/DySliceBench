def examB():
    N = I(); s = [S() for _ in range(N)]
    M = I(); t = [S() for _ in range(M)]
    d = defaultdict(int)
    for l in s:
        d[l] +=1
    for l in t:
        d[l] -=1
    ans = max(0,max(d.values()))
    print(ans)


import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
