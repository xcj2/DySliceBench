def examC():
    N, Y = LI()
    ans = [-1, -1, -1]
    for i in range(N+1):
        for j in range(N-i+1):
            cur = 10000*i + 5000*j + 1000*(N-i-j)
            if Y==cur:
                ans = [i,j,(N-i-j)]
                break
    print(" ".join(map(str,ans)))

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
