def examC():
    N = I()
    C = [0]*N; S =[0]*N; F = [0]*N
    for i in range(N-1):
        C[i], S[i], F[i] = LI()
    ans = []
    for i in range(N):
        cur = 0
        for j in range(i,N-1):
            cur = max(((cur-1)//F[j] +1)*F[j],S[j])+C[j]
        ans.append(cur)
    for v in ans:
        print(v)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
