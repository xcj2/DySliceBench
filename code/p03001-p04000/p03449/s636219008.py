def examC():
    N = I()
    A1 = LI(); A2 = LI()
    ans = 0
    for i in range(N+1):
        cur = sum(A1[:(i+1)]) + sum(A2[i:])
        ans = max(ans,cur)
    print(ans)


import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
