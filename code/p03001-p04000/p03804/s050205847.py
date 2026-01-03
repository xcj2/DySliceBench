def examB():
    N, M = LI()
    A = [S() for _ in range(N)]
    B = [S() for _ in range(M)]
    loop = N-M+1
    ans = "No"
    for i in range(loop):
        for j in range(loop):
            cur = int(0)
            for k1 in range(M):
                for k2 in range(M):
                    if A[i+k1][j+k2]==B[k1][k2]:
                        cur +=1
            if cur==M**2:
                ans = "Yes"
    print(ans)

import sys
import copy
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examB()
