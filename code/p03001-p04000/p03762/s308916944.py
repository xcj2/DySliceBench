def examD(mod):
    n, m = LI()
    x = LI()
    y = LI()
    ans = 0; ans1 = 0; ans2 = 0
    for i in range(n-1):
        surface = (x[i+1]-x[i])*(n-1-i)*(i+1)
        ans1 = (ans1+surface)%mod
    for i in range(m-1):
        surface = (y[i+1]-y[i])*(m-1-i)*(i+1)
        ans2 = (ans2+surface)%mod
    ans = ans1*ans2%mod
    print(ans)

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

examD(mod)