def examC():
    N = I()
    A = LI()
    cost1 = [0]*(N+1); cost2 = [0]*(N+1)
    A.append(0)
    for i in range(N+1):
        cost1[i] = abs(A[i]-A[i-1])
        cost2[i] = abs(A[i]-A[i-2])
    ans = []
    cost = sum(cost1)
    for i in range(N):
        cur = cost - cost1[i] - cost1[i+1] + cost2[i+1]
        ans.append(cur)
    for v in ans:
        print(v)

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
