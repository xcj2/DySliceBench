def examB():
    N, A, B = LI()
    cur = 0
    for i in range(1,N+1):
        judge = 0; icur = i
        while(icur>0):
            judge +=icur%10
            icur //=10
        if A<=judge<=B:
            cur +=i
    print(cur)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
