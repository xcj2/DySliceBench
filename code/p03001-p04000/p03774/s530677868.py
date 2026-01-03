def examB(inf):
    N, M = LI()
    ab = [LI() for _ in range(N)]
    cd = [LI() for _ in range(M)]
    ans = []
    for i in range(N):
        cur = inf
        for j in range(M):
            k = abs(ab[i][0]-cd[j][0]) + abs(ab[i][1]-cd[j][1])
            if cur>k:
                cur = k
                ansC = j
        ans.append(ansC+1)
    for v in ans:
        print(v)

import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB(inf)
