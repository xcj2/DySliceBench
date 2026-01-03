def pff(m):
    pf = {}
    for i in range(2, int(m ** 0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1: pf[m] = 1
    return pf

def examC(mod):
    N = I()
    ans = int(1)
    d = defaultdict(int)
    for i in range(2,N+1):
        m = pff(i)
#        print(m)
        for v in m:
            d[v] += m[v]
#    print(d)
    for i in d:
        ans = (ans*(d[i]+1))%mod
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

examC(mod)
