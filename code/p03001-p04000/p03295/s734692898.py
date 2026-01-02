def examD():
    N, M = LI()
    right = defaultdict(int)
    for _ in range(M):
        a, b = LI()
        right[b] = max(right[b],a)
    ans = 0; cur = 0
    for i in range(1,N+1):
        if right[i]>cur:
            ans +=1
            cur = i-1
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
