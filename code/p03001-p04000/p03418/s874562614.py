def examD():
    N, K =LI()
    cur = 0
    for i in range(K+1,N+1):
        cur +=((N//i)*(i-K) + max(0,N%i-K+1))
#        print(cur,i)
    if K==0:
        cur -=N
    print(cur)

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

examD()
