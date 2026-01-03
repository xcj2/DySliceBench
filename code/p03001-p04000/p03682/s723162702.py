def find(A,x) -> int:
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a

def union(A, x, y):
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx
def examD():
    N = I()
    x = [[] for _ in range(N)]; y = [[] for _ in range(N)]
    for i in range(N):
        a, b = LI()
        x[i] = (a-1,i)
        y[i] = (b-1,i)
    v = [ i for i in range(N)]
    x.sort(); y.sort()
    H = []
    heapify(H)
    for i in range(N - 1):
        x1, j1 = x[i]
        x2, j2 = x[i + 1]
        y1, k1 = y[i]
        y2, k2 = y[i + 1]
        heappush(H, (x2 - x1, j1, j2))
        heappush(H, (y2 - y1, k1, k2))
    ans = 0
#    print(H)
#    print(v)
    while H:
        w, s, t = heappop(H)
        if find(v, s) != find(v, t):
            union(v, s, t)
            ans += w
    print(ans)

import sys
import copy
import bisect
from heapq import *
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
