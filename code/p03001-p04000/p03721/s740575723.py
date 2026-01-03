def examC():
    N, K = LI()
    d = defaultdict(int)
    element = set()
    for _ in range(N):
        a, b = LI()
        d[a] += b
        element.add(a)
    element = list(element)
    element.sort()
    for i in element:
        K -= d[i]
        if K<=0:
            ans = i
            break
    print(ans)
#    print(element)

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

examC()
