def examB(inf):
    N = I()
    A = LI()
    sumA = sum(A)
    cur = 0
    need = inf
    for i in range(N):
        need = min(need,abs(cur*2-sumA))
        cur += A[i]
    print(need)

def examC():
    return

def examD():
    return

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

examB(inf)