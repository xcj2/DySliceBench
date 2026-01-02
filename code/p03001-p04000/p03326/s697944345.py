def examD():
    N, M = LI()
    X = [LI() for _ in range(N)]
    ans = 0
    for a in [-1,1]:
        for b in [-1,1]:
            for c in [-1,1]:
                que = []; ansC = 0
                for i in X:
                    cur = a*i[0] + b*i[1] + c*i[2]
                    heapq.heappush(que,-cur)
                for j in range(M):
                    ansC -= heapq.heappop(que)
                ans = max(ans,ansC)
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
