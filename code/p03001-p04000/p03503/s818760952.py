def examC(inf):
    N = I()
    F = [LI() for _ in range(N)]
    P = [LI() for _ in range(N)]
    loop = 2**10
    ans = -inf
    for i in range(1,loop):
        cur = [0]*N
        for j in range(10):
            if (i>>j)&1==1:
                for k in range(N):
                    if F[k][j]==1:
                        cur[k]+=1
        ansC =0
        for j in range(N):
            ansC += P[j][cur[j]]
        ans = max(ans,ansC)
    print(ans)


import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC(inf)
