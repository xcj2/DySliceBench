def examD():
    M = I()
    cur = 0; ans = 0
    for i in range(M):
        c, d = LI()
        cur += d*c
        ans += d
    ans += (cur-1)//9 -1
    print(ans)

def examE():
    return

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
