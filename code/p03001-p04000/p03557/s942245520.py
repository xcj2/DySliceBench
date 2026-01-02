def examC():
    N = I()
    A = LI(); B = LI(); C = LI()
    A.sort(); B.sort(); C.sort()
    ans = 0
    for i in range(N):
        ans += bisect.bisect_left(A, B[i]) * (N - bisect.bisect_right(C, B[i]))
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

examC()
