def examC():
    N, K = LI()
    A = LI()
    d = defaultdict(int)
    for i in A:
        d[i] +=1
    cur = 0
    que = []
    heapq.heapify(que)
    for i in d.values():
        heappush(que,i)
    for i in range(len(d)-K):
        cur += heappop(que)
    print(cur)

import sys,copy,bisect,itertools,heapq
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
