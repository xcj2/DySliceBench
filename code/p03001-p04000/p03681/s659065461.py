def examC(mod):
    N, M = LI()
    fac = [1]*max(N,M)
    for i in range(1,max(N,M)):
        fac[i] = (i+1)*fac[i-1]%mod
    if abs(N-M)==1:
        ans = fac[N-1]*fac[M-1]%mod
    elif abs(N-M)==0:
        ans = fac[N-1]*fac[M-1]*2%mod
    else:
        ans = 0
    print(ans)

import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC(mod)
