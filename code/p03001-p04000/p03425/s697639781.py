def examC():
    N = I()
    St = [S() for _ in range(N)]
    d = defaultdict(int)
    ans = 0
    march = ["M","A","R","C","H"]
    for s in St:
        if s[0] in march:
            d[s[0]] +=1
    if len(d)>=3:
        for comb in itertools.permutations(march):
            ans += d[comb[0]]*d[comb[1]]*d[comb[2]]
        ans //=12
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

examC()
