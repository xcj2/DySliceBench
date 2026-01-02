def examB():
    N = I()
    St = LS()
    d = defaultdict(str)
    for s in St:
        d[s] = 1
    if len(d)==3:
        ans = "Three"
    elif len(d)==4:
        ans = "Four"
    if ans:
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
